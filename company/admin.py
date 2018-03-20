from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Company)
admin.site.register(models.Pallet)
admin.site.register(models.Transaction)
