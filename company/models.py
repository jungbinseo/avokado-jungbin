from django.db import models

# Create your models here.

class Company(models.Model):
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.code

class Pallet(models.Model):
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.code

class Transaction(models.Model):
    CLASSIFIED_CHOICES = (
        ('계약처','계약처'),
    )
    classified = models.CharField(max_length=5, choices=CLASSIFIED_CHOICES)
    TYPE_CHOICES = (
        ('납품(직송포함)','납품'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField('date out')
    pallet = models.ForeignKey(Pallet, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
