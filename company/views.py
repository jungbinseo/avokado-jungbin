from django.shortcuts import render
from rest_framework import viewsets, generics

from . import models
from . import serializers

# Create your views here.

class CompanyListCreateView(generics.ListCreateAPIView):   
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()
    
class CompanyRetrieveView(generics.RetrieveUpdateDestroyAPIView):   
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()
