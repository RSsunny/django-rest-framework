from django.contrib import admin
from .models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'author')
    list_filter = ('is_published', 'created_at')

admin.site.register(Blog, BlogAdmin)