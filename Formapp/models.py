from django.db import models

# Create your models here.
class StudentData(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    created_at=models.DateField()