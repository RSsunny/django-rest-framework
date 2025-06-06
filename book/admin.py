from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date', 'isbn', 'pages', 'cover_image', 'language')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('published_date', 'language')

admin.site.register(Book, BookAdmin)