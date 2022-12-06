from django.db import models
from django.utils.timezone import now


class Feedback(models.Model):
    count = models.FloatField(default=1)
    name = models.CharField(max_length=255)
    date = models.DateField(default=now)
    description = models.TextField()
    category = models.CharField(max_length=50)
