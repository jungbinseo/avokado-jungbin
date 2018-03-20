from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Sum, Avg

from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

from . import models
from . import serializers

# Create your views here.
class ProductPagination(LimitOffsetPagination):
    page_size = 100

class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.annotate(count = Count('transaction'), sum=Sum('transaction__amount'))
    pagination_class = ProductPagination

class CompanyApiView(APIView):
    serializer_class = serializers.CompanySerializer

    def get(self, request, format=None):
        companys = models.Company.objects.all()
        paginator = Paginator(companys,50)
        page = request.GET.get('page')

        try:
            companys = paginator.page(page)
        except PageNotAnInteger:
            companys = paginator.page(1)
        except EmptyPage:
            companys = paginator.page(paginator.num_pages)
        serializer = serializers.CompanySerializer(companys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()


class PalletListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.PalletSerializer
    queryset = models.Pallet.objects.annotate(count = Count('transaction'), sum=Sum('transaction__amount'))

class PalletRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PalletSerializer
    queryset = models.Pallet.objects.all()


class TransactionListView(generics.ListAPIView):
    serializer_class = serializers.TransactionSerializer
    queryset = models.Transaction.objects.all()

    def get_queryset(self):
        transactions = self.queryset.values('company__code', 'pallet__code'
        ).annotate(sum = Sum('amount'), count = Count('id'))
        return transactions
