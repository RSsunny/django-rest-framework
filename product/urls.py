from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_list, name='product_detail')
]
