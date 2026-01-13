from django.shortcuts import render
from rest_framework import serializers
from .models import Products
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer

# Create your views here.


class ProductList(APIView):
  def get(self, request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response(serializer.data)
  

class ProductDetail(APIView):
    def get(self, request, pk):
        try:
            product = Products.objects.get(pk=pk)  
        except Products.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
        
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    

