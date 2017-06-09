from __future__ import unicode_literals

from django.db import models
from lims import settings


class User(models.Model):
    user = models.OneToOneField("auth.User")
    phone = models.CharField(max_length=64, blank=True, null=True)


class Department(models.Model):
    name = models.CharField(max_length=256)


class Subscription(models.Model):
    pass


class Instrument(models.Model):
    INSTRUMENT_STATUS_CHOICES = (
        ('R', 'ready'),
        ('O', 'occupied'),
        ('U', 'unavailable')
    )
    name = models.CharField(max_length=256)
    # todo admin m2m
    status = models.CharField(max_length=64, choices=INSTRUMENT_STATUS_CHOICES, default='R')
    department = models.ForeignKey(Department, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to=settings.UPLOAD_FOLDER, max_length=256)
    admin = models.ForeignKey(User)
    description = models.TextField(blank=True, null=True)
