from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
# Create your views here.
class UserList(GenericAPIView, ListModelMixin):
     queryset= User.objects.all()
     serializer_class = UserSerializer
     def get(self, request, *args, **kwargs):
         return self.list(request, *args, **kwargs)

class UserListView(GenericAPIView,CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)