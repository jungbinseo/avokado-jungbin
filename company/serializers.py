from rest_framework import serializers

from . import models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('id', 'code')

class PalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pallet
        fields = ('id', 'code')

