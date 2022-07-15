import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CardControl.settings')

app = Celery('CardControl')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-card-every-1-day': {
        'task': 'core.tasks.check_beat_card',
        'schedule': crontab(minute=0, hour=0)
    }
}
