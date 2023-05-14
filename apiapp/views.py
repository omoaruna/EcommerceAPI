from django.shortcuts import render
from .models import *
from .serializer import ProductSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class api_home_page(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class api_details_page(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

# Create your views here.
