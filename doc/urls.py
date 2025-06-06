from django.urls import path
from .views import DocumentListView, DocumentDetailView
urlpatterns = [
    path('doc/', DocumentListView.as_view(), name='document_list'),
    path('doc/<int:pk>/', DocumentDetailView.as_view(), name='document_detail'),
]
