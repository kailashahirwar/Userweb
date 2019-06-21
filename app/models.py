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


class ContentType(models.Model):
    name = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'content_types'


class Content(models.Model):
    content = models.TextField(default="", null=False)
    type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'contents'
