from urllib.parse import urlsplit

from celery.result import AsyncResult
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from brokers.celery import app
from jobs.tasks import add, build_report


def redact(url):
    if not url:
        return ''
    parts = urlsplit(url)
    if parts.password:
        netloc = parts.netloc.replace(f':{parts.password}@', ':****@')
        return parts._replace(netloc=netloc).geturl()
    return url


def home_view(request):
    cache.add('page_views', 0, timeout=None)
    page_views = cache.incr('page_views')

    context = {
        'broker_url': redact(settings.CELERY_BROKER_URL),
        'result_backend': redact(settings.CELERY_RESULT_BACKEND),
        'cache_backend': settings.CACHES['default']['BACKEND'].rsplit('.', 1)[-1],
        'page_views': page_views,
        'task_ids': request.session.get('task_ids', []),
    }
    return render(request, 'home.html', context)


@require_POST
def enqueue_view(request):
    if request.POST.get('kind') == 'report':
        result = build_report.delay(rows=5)
    else:
        result = add.delay(2, 3)

    request.session['task_ids'] = [result.id] + request.session.get('task_ids', [])[:9]
    return redirect('home')


def task_status_view(request, task_id):
    result = AsyncResult(task_id, app=app)
    payload = {'id': task_id, 'state': result.state}
    if result.state == 'PROGRESS':
        payload['meta'] = result.info
    elif result.successful():
        payload['result'] = result.result
    elif result.failed():
        payload['error'] = str(result.result)
    return JsonResponse(payload)


def health_view(request):
    checks = {}

    try:
        with app.connection_for_write() as conn:
            conn.ensure_connection(max_retries=1)
        checks['broker'] = 'ok'
    except Exception as exc:
        checks['broker'] = f'error: {exc}'

    try:
        cache.set('health_check', 'ok', timeout=5)
        checks['cache'] = 'ok' if cache.get('health_check') == 'ok' else 'error: value not stored'
    except Exception as exc:
        checks['cache'] = f'error: {exc}'

    healthy = all(value == 'ok' for value in checks.values())
    return JsonResponse(checks, status=200 if healthy else 503)
