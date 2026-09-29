import time

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task(bind=True)
def build_report(self, rows=5):
    for done in range(1, rows + 1):
        time.sleep(1)
        self.update_state(state='PROGRESS', meta={'done': done, 'total': rows})
    return {'done': rows, 'total': rows}
