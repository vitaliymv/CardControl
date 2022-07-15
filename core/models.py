from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Card(models.Model):
    series = models.CharField(max_length=3)
    number = models.PositiveBigIntegerField()
    release_date = models.DateTimeField()
    activity_end_date = models.DateTimeField()
    cvv = models.IntegerField()
    funds = models.IntegerField()
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.number.__str__()


class Purchase(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    address = models.CharField(max_length=255)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)

    def __str__(self):
        return self.card.number.__str__()
