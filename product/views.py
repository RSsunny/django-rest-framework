from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here
@api_view(['GET'])
def product_list(request,pk=None):
    if request.method == 'GET':
        if pk is not None:
            product= Product.objects.get(id=pk)
            serializer= ProductSerializer(product)
            return Response(serializer.data)
        products= Product.objects.all()
        serializer= ProductSerializer(products, many=True)
        return Response(serializer.data)



        