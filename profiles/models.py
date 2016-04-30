from django.db import models
from django.contrib.auth.models import User

from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User,
            on_delete=models.CASCADE)
    perfered_name = models.CharField(max_length=100)
    birthdate = models.DateField(default=date.today)
    interests = models.CharField(max_length=100)
    STATE_CHOICES = (
            ('GA', 'GA'),
            ('NC', 'NC'),
            ('SC', 'SC'),
            ('TN', 'TN'),
            ('VA', 'VA'),
            ('WV', 'WV'),
        )
    state_of_residence = models.CharField(max_length=2,
            choices=STATE_CHOICES, default='NC')

    def __str__(self):
        return self.perfered_name

