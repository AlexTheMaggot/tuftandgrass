from django.urls import path
from . import views


app_name = 'mainapp_en'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:post_id>/', views.news_detail, name='news_detail'),
    path('catalog/', views.category_list, name='category_list'),
    path('catalog/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('catalog/<slug:category_slug>/<slug:subcategory_slug>/', views.subcategory_detail, name='subcategory_detail'),
    path('catalog/<slug:category_slug>/<slug:subcategory_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
