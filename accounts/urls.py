from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('password/', views.password, name='password'),
]