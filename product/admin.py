from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'created_at', 'updated_at', 'is_active', 'cat_id')
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('-created_at',)
    list_editable = ('is_active',)
    list_per_page = 10
    date_hierarchy = 'created_at'
   

admin.site.register(Product, ProductAdmin)