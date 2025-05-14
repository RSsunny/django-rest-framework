from django.shortcuts import render
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
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