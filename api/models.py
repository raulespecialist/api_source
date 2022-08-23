from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Email(models.Model):
    email = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now)
    email_status = models.CharField(max_length=200)
    email_score = models.IntegerField(verbose_name='Email Score')
    valid_email = models.BooleanField(default=False)
    fraud = models.BooleanField(default=False)

    def __str__(self):
        return self.email