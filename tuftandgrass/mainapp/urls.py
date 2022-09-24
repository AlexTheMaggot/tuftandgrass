from django.urls import path
from . import views


app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:post_id>/', views.news_detail, name='news_detail'),
    path('catalog/', views.category_list, name='category_list'),
    path('catalog/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('catalog/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('order/', views.order, name='order'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
