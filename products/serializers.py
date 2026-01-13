from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
      model = Products
      fields = '__all__'

