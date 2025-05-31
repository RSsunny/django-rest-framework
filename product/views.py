from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here
@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def product_list(request,pk=None):
    if request.method == 'GET':
        if pk is not None:
            product= Product.objects.get(id=pk)
            serializer= ProductSerializer(product)
            return Response(serializer.data)
        products= Product.objects.all()
        serializer= ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Product created successfully'}
            return Response(res, status=201)
        return Response(serializer.errors, status=400)
    if request.method == 'PUT':
        product = Product.objects.get(id=pk)
        serializer= ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Product updated successfully'}
            return Response(res, status=200)
        return Response(serializer.errors, status=400)
    if request.method == 'PATCH':
        product = Product.objects.get(id=pk)
        serializer= ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Product updated successfully'}
            return Response(res, status=200)
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        product = Product.objects.get(id=pk)
        product.delete()
        res={'msg':'Product deleted successfully'}
        return Response(res, status=204)

        