from django.urls import path

from jobs.views import enqueue_view, health_view, home_view, task_status_view

urlpatterns = [
    path('', home_view, name='home'),
    path('enqueue/', enqueue_view, name='enqueue'),
    path('tasks/<str:task_id>/', task_status_view, name='task_status'),
    path('health/', health_view, name='health'),
]
