from django.urls import path
from . import views


app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news_list, name='news_list'),
    path('order/', views.order, name='order'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
