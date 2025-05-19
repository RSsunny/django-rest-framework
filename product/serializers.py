from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields= '__all__'
        # fields= ['id', 'title', 'description', 'price', 'created_at', 'updated_at', 'is_active', 'cat_id']    
        


