from django.urls import path
from . import views


app_name = 'mainapp_uz'

urlpatterns = [
    path('', views.index, name='index'),
]