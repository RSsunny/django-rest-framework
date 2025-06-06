from django.urls import path
from .views import UserListView, UserList
urlpatterns = [
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>', UserListView.as_view(), name='user_retrieve'),
    # Add more user-related URLs here as needed
]