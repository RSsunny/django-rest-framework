from django.contrib import admin
from .models import Teacher
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'subject', 'time', 'date', 'phone', 'email', 'address')
    search_fields = ('name', 'subject')
    list_filter = ('subject',)
    ordering = ('name',)
    list_per_page = 10


    


admin.site.register(Teacher, TeacherAdmin)