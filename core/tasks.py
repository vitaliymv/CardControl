from django.utils import timezone

from CardControl.celery import app
from core.models import Card


@app.task
def check_beat_card():
    cards = Card.objects.all()
    for card in cards:
        if card.activity_end_date < timezone.now():
            card.status = 'Overdue'
        card.save()
