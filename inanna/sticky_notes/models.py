from django.db import models


# Create your models here.
class StickyNotes(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(max, blank=True)
