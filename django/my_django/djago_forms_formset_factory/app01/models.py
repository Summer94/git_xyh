from django.db import models

# Create your models here.

class Publisher(models.Model):
    title = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
