from rest_framework import serializers
from .models import Book  # Import the Book model from the models module in the book app
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book # Assuming the model is named Book in the book app
        fields = '__all__'  # Include all fields from the Book model