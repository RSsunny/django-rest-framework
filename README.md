## <h1 align="center">Django Rest Framework</h1>

## Django REST framework is a powerful and flexible toolkit for building Web APIs. Some reasons you might want to use REST framework:

### step by step guideline

- setup virtual enviroment

  ```
  python -m venv env
  ```

- Create Folder

  ```
  mkdir folder_name
  ```

- navigate folder

  ```
  cd folder_name
  ```

- install django

  ```
  pip install django
  ```

- create project

  ```
  django-admin startproject project_name
  ```

- install rest framework

  ```
  pip install djangorestframework
  ```

- setup url rest framework

  ```
  INSTALLED_APPS = [
      ...
      'rest_framework',
  ]
  ```

- url

  ```
      urlpatterns = [
          ...
          path('api-auth/', include('rest_framework.urls'))
      ]
  ```

## Serializers structure

```
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
```

## Model Serializers Structure

```
    from rest_framework import serializers
    from .models import Product

    class ProductSerializer(serializers.ModelSerializer):
          class Meta:
              model =Product
              fields= '__all__'
              # fields= ['id', 'title', 'description', 'price', 'created_at', 'updated_at', 'is_active', 'cat_id']

```
