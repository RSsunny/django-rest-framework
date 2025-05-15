from rest_framework import serializers
from . models import Teacher
class TeacherSerializer(serializers.Serializer):
      name= serializers.CharField(max_length=100)
      subject= serializers.CharField(max_length=100)
      time= serializers.TimeField()
      date= serializers.DateField()
      phone= serializers.CharField(max_length=15)
      email= serializers.EmailField()
      address= serializers.CharField(max_length=200)
      def create(self, validated_data):
            return Teacher.objects.create(**validated_data)