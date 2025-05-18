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
      def update(self, instance, validated_data):
            instance.name=validated_data.get('name', instance.name)
            instance.subject=validated_data.get('subject', instance.subject)
            instance.time=validated_data.get('time', instance.time)
            instance.date=validated_data.get('date', instance.date)
            instance.phone=validated_data.get('phone', instance.phone)
            instance.email=validated_data.get('email', instance.email)
            instance.address=validated_data.get('address', instance.address)
            instance.save()
            return instance