from django.db import models

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todolist(models.Model):

    name = models.CharField(max_length=500)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now())
    duedate = models.DateField(default=timezone.now())
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name