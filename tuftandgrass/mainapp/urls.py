from django.urls import path
from . import views


app_name = 'mainapp'

urls = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:post_id>/', views.news_detail, name='news_detail'),
    path('catalog/', views.category_list, name='category_list'),
    path('catalog/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('catalog/<slug:category_slug>/<slug:subcategory_slug>/', views.subcategory_detail, name='subcategory_detail'),
    path('catalog/<slug:category_slug>/collections/<slug:collection_slug>/',
         views.collection_detail, name='collection_detail'),
    path('catalog/<slug:category_slug>/<slug:subcategory_slug>/<slug:collection_slug>/',
         views.collection_detail_sub, name='collection_detail_sub'),
    path('catalog/<slug:category_slug>/collections/<slug:collection_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
    path('catalog/<slug:category_slug>/<slug:subcategory_slug>/<slug:collection_slug>/<slug:product_slug>/',
         views.product_detail_sub, name='product_detail_sub'),
]

order_urls = [
    path('order/', views.order, name='order'),
    path('subscribe/', views.subscribe, name='subscribe'),
]

urlpatterns = urls + order_urls
