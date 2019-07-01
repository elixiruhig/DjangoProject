from django.db import models

# Create your models here.
class Run(models.Model):
    steps = models.IntegerField(default=0)