from django.db import models

# Create your models here.

class Book(models.Model):
  id = models.AutoField(primary_key=True)
  title= models.CharField(max_length=50)
  description= models.TextField(max_length=100)
  rate= models.IntegerField()
  views= models.IntegerField()
