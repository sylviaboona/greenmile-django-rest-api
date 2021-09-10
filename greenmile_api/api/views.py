from django.shortcuts import render
from rest_framework import generics
from .models import Loader, Supplier, Package
from .serializers import LoaderSerializer, SupplierSerializer, PackageSerializer

# Create your views here.
class LoadersList(generics.ListCreateAPIView):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer

class SuppliersList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class PackagesList(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
