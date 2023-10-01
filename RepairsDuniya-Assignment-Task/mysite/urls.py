from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('users/', views.list_or_get_user, name='list-users'),
    path('users/<int:id>/', views.list_or_get_user, name='get-user-by-id'),
    path('users/create/', views.create_user, name='create-user'),
    path('users/update/<int:id>/', views.update_user, name='update-user'),
    path('users/delete/<int:id>/', views.delete_user, name='delete-user'),
]
