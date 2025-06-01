from django.urls import path
from . import views
urlpatterns = [
    path('blogs/', views.BlogList.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', views.BlogList.as_view(), name='blog_detail'),
]
