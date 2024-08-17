from django.db import models

# Create your models here.
class Car(models.Model):
    marca = models.TextField(max_length=100)