from django.db import models

# Create your models here.
class Question(models.Model):
    que = models.CharField(max_length=1000,blank=False,null=False)
    option1 = models.CharField(max_length=500,blank=False,null=False)
    option2 = models.CharField(max_length=500, blank=False, null=False)
    option3 = models.CharField(max_length=500, blank=False, null=False)
    option4 = models.CharField(max_length=500, blank=False, null=False)
    answer = models.CharField(max_length=3,blank=True)
    correct = models.CharField(max_length=3,blank=True)