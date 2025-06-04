from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('-created_at',)

admin.site.register(User, UserAdmin)