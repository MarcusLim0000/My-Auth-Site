from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_user/', views.create_user, name='create_user'),
    path('register/', views.register, name='register'),
    path('view/', views.view, name='view'),
    path('login/', views.user_login, name='login'),
    path('permission_error/', views.permission_error, name='permission_error'),
]
