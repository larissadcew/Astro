from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Login/', views.Login, name='Login'),
    path('Registrar/', views.register, name='Register'),
    path('Eventos/', views.Eventos, name='Eventos'),
    path('new/', views.new, name='new'),



]
