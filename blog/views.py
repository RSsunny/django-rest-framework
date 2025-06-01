from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class BlogList(APIView):
    def get(self, request,pk=None, *args, **kwargs): 
            if pk is not None:
                # Fetch a single blog post by primary key
                blog= Blog.objects.get(id=pk)
                serializer= BlogSerializer(blog)
                return Response(serializer.data)
            blogs= Blog.objects.all()
            serializer= BlogSerializer(blogs, many=True)
            return Response(serializer.data)