from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from .models import Document
from .serializers import DocumentSerializer
# Create your views here.
class DocumentListView(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
class DocumentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer