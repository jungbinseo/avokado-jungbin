from django.db import models

# Create your models here.

class Company(models.Model):
    code = models.CharField(max_length=255)
