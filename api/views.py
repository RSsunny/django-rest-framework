from django.shortcuts import render
from .models import Teacher
from .serializers import TeacherSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
# Create your views here.
def teacher_list(request):
    # complex data get
    ts= Teacher.objects.all()
    # python dict
    serialized_data = TeacherSerializer(ts, many=True)
    # json data
    json_data = JSONRenderer().render(serialized_data.data)
    # returning json data
    return HttpResponse(json_data, content_type='application/json' ,)


def SingleTeacher(request,id):
    # complex data get
    ts= Teacher.objects.get(id=id)
    # python dict
    serialized_data = TeacherSerializer(ts)
    # json data
    json_data = JSONRenderer().render(serialized_data.data)
    # returning json data
    return HttpResponse(json_data, content_type='application/json' ,)

@csrf_exempt
def teacher_create(request):
    if request.method == 'POST':
        data= request.body
        print(f'data: {data}')
        # stream data
        stream_data= io.BytesIO(data)
        print(f'stream_data: {stream_data}')
        # python dict
        python_data=JSONParser().parse(stream_data)
        print(f'python_data: {python_data}')
        # serializer
        serialized_data= TeacherSerializer(data=python_data , many=True)
        # validation
        if serialized_data.is_valid():
            serialized_data.save()
            response= {'msg':'Data Created'}
            json_data=JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application.json')
        response= {'msg':'Data Not Created'}
        json_data=JSONRenderer().render(response)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'PUT':
        data=request.body
        # stream data
        stream_data= io.BytesIO(data)
        # python dict
        python_data=JSONParser().parse(stream_data)
        id= python_data.get('id')
        id_match= Teacher.objects.get(id=id)
        # serializer
        serialized_data= TeacherSerializer(id_match, data=python_data, partial=True)
        # validation   
        if serialized_data.is_valid():
            serialized_data.save()
            response= {'msg':'Data Updated'}
            json_data=JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application.json')
