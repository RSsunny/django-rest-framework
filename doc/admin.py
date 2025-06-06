from django.contrib import admin
from .models import Document
# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'author')
    list_filter = ('is_published', 'created_at')
admin.site.register(Document, DocumentAdmin)