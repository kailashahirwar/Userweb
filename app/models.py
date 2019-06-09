from django.db import models
from django.utils import timezone


class Interest(models.Model):
    name = models.CharField(max_length=200, default="", null=False, name="name")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'interests'


class Requirement(models.Model):
    name = models.CharField(max_length=200, default="", null=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'requirements'
