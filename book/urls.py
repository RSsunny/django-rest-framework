from django.urls import path
from .views import BookCrudView
urlpatterns = [
    path('books/', BookCrudView.as_view(), name='book-list'),
]
