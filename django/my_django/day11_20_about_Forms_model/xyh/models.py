from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Pub(models.Model):
    name = models.CharField(max_length=12)
    addr = models.CharField(max_length=255)


