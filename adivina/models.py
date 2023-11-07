from django.db import models

# Create your models here.
class adivina(models.Model):
    number_secret = models.IntegerField()
    attempts = models.IntegerField(default=0)