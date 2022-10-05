from django.db import models
from django.forms import CharField


class Archive(models.Model):
    title = CharField(max_length=120)
    archive_field = models.FileField(upload_to ='uploads/')