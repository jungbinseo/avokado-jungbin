from rest_framework import serializers

from . import models

class CompanySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255)
    sum = serializers.IntegerField(default=0)
    count = serializers.IntegerField(default=0)

class PalletSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255)
    sum = serializers.IntegerField(default=0)
    count = serializers.IntegerField(default=0)

class TransactionSerializer(serializers.Serializer):
    company__code = serializers.CharField()
#    date = serializers.DateField()
    pallet__code = serializers.CharField()
#    amount = serializers.IntegerField(default=0)
    sum = serializers.IntegerField(default=0)
    count = serializers.IntegerField(default=0)
