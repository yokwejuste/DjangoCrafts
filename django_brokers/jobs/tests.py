from unittest import mock

from django.test import TestCase, override_settings

from jobs.tasks import add, build_report
from jobs.views import redact

LOCMEM = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}


class TaskTests(TestCase):
    def test_add_runs_locally(self):
        self.assertEqual(add.apply(args=(2, 3)).get(), 5)

    @mock.patch('jobs.tasks.time.sleep')
    def test_build_report_reports_all_rows(self, _sleep):
        with mock.patch.object(build_report, 'update_state'):
            self.assertEqual(build_report.apply(kwargs={'rows': 3}).get(), {'done': 3, 'total': 3})


class RedactTests(TestCase):
    def test_hides_password(self):
        self.assertEqual(redact('amqp://guest:secret@localhost:5672//'), 'amqp://guest:****@localhost:5672//')

    def test_leaves_url_without_password(self):
        self.assertEqual(redact('redis://localhost:6379/0'), 'redis://localhost:6379/0')


@override_settings(CACHES=LOCMEM)
class ViewTests(TestCase):
    def test_home_counts_page_views(self):
        self.client.get('/')
        response = self.client.get('/')
        self.assertEqual(response.context['page_views'], 2)

    @mock.patch('jobs.views.add.delay')
    def test_enqueue_stores_task_id(self, delay):
        delay.return_value.id = 'abc123'
        self.client.post('/enqueue/', {'kind': 'add'})
        self.assertEqual(self.client.session['task_ids'], ['abc123'])
