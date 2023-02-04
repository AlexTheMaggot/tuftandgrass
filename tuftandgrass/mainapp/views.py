from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.core.paginator import Paginator
from tuftandgrass.config import *
from .models import *
from .forms import *
import requests


def make_context(context):
    posts = NewsModel.objects.all().order_by('-date')
    context['three_posts'] = Paginator(posts, 3).page(1)
    context['header'] = HeaderModel.objects.first()
    context['footer'] = FooterModel.objects.first()
    context['indexpage'] = IndexPageModel.objects.first()
    return context


def custom_404(request, exception):
    template = 'mainapp/404.html'
    context = {}
    context = make_context(context)
    return render(request, template, context)


def index(request):
    template = 'mainapp/index.html'
    context = {
        'slides': IndexPageSlideModel.objects.all(),
        'products': IndexPageProductModel.objects.all(),
        'faqs': IndexPageFAQModel.objects.all(),
        'team': IndexPageTeamUnitModel.objects.all(),
        'reviews': ReviewModel.objects.all(),
    }
    context = make_context(context)
    return render(request, template, context)


def about(request):
    template = 'mainapp/about.html'
    context = {
        'aboutpage': AboutPageModel.objects.first(),
        'reviews': ReviewModel.objects.all(),
        'products': IndexPageProductModel.objects.all(),
    }
    context = make_context(context)
    return render(request, template, context)


def contacts(request):
    template = 'mainapp/contacts.html'
    context = {
        'contactspage': ContactsPageModel.objects.first()
    }
    context = make_context(context)
    return render(request, template, context)


def news_list(request):
    template = 'mainapp/news_list.html'
    context = {
        'posts': NewsModel.objects.all().order_by('-date'),
        'newspage': NewsListPageModel.objects.first(),
    }
    context = make_context(context)
    return render(request, template, context)


def news_detail(request, post_id):
    template = 'mainapp/news_detail.html'
    context = {
        'post': get_object_or_404(NewsModel, id=post_id),
    }
    context = make_context(context)
    return render(request, template, context)


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            tg_bot_token = TG_BOT_TOKEN
            tg_chat = '-1001613901910'
            tg_message = 'Новая заявка с сайта!\n\nИмя: {0}\nНомер телефона: {1}\n'.format(
                request.POST['name'], request.POST['phone']
            )
            if request.POST['email'] != '':
                tg_message += 'E-mail: {0}\n'.format(request.POST['email'])
            if request.POST['text'] != '':
                tg_message += 'Сообщение: {0}\n'.format(request.POST['text'])
            tg_url = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(
                tg_bot_token, tg_chat, tg_message)
            requests.get(tg_url)
            return HttpResponse(request, 'Success')
    else:
        return HttpResponseForbidden(request)


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            tg_bot_token = TG_BOT_TOKEN
            tg_chat = '-1001613901910'
            tg_message = 'Новая подписка!\n\nПочта: {0}'.format(request.POST['email'])
            tg_url = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(
                tg_bot_token, tg_chat, tg_message)
            requests.get(tg_url)
            return HttpResponse(request, 'Success')
    else:
        return HttpResponseForbidden(request)


def category_list(request):
    template = 'mainapp/category_list.html'
    context = {
        'categorylistpage': CategoryListPageModel.objects.first(),
        'categories': CategoryModel.objects.all(),
    }
    context = make_context(context)
    return render(request, template, context)


def category_detail(request, category_slug):
    template = 'mainapp/category_detail.html'
    products = ProductModel.objects.all().filter(collection__category__slug=category_slug)
    collections = CollectionModel.objects.all().filter(category__slug=category_slug)
    subcategories = SubcategoryModel.objects.all().filter(category__slug=category_slug)
    if 'sort' in request.GET:
        products = products.order_by(request.GET['sort'])
        collections = collections.order_by(request.GET['sort'])
        subcategories = subcategories.order_by(request.GET['sort'])
    else:
        collections = collections.order_by('-id')
    context = {
        'category': get_object_or_404(CategoryModel, slug=category_slug),
        'categories': CategoryModel.objects.all(),
        'products': products,
        'collections': collections,
        'subcategories': subcategories,
    }
    context = make_context(context)
    return render(request, template, context)


def subcategory_detail(request, category_slug, subcategory_slug):
    collections = CollectionModel.objects.all().filter(subcategory__slug=subcategory_slug)
    if 'sort' in request.GET:
        collections = collections.order_by(request.GET['sort'])
    template = 'mainapp/subcategory_detail.html'
    context = {
        'category': get_object_or_404(CategoryModel, slug=category_slug),
        'subcategory': get_object_or_404(SubcategoryModel, slug=subcategory_slug),
        'collections': collections,
    }
    context = make_context(context)
    return render(request, template, context)


def collection_detail(request, category_slug, collection_slug):
    template = 'mainapp/collection_detail.html'
    products = ProductModel.objects.all().filter(collection__slug=collection_slug)
    if 'sort' in request.GET:
        products = products.order_by(request.GET['sort'])
    context = {
        'category': get_object_or_404(CategoryModel, slug=category_slug),
        'categories': CategoryModel.objects.all(),
        'collection': get_object_or_404(CollectionModel, slug=collection_slug),
        'products': products,
    }
    context = make_context(context)
    return render(request, template, context)


def collection_detail_sub(request, category_slug, subcategory_slug, collection_slug):
    template = 'mainapp/collection_detail.html'
    products = ProductModel.objects.all().filter(collection__slug=collection_slug)
    if 'sort' in request.GET:
        products = products.order_by(request.GET['sort'])
    context = {
        'category': get_object_or_404(CategoryModel, slug=category_slug),
        'subcategory': get_object_or_404(SubcategoryModel, slug=subcategory_slug),
        'categories': CategoryModel.objects.all(),
        'collection': get_object_or_404(CollectionModel, slug=collection_slug),
        'products': products,
    }
    context = make_context(context)
    return render(request, template, context)


def product_detail(request, category_slug, collection_slug, product_slug, subcaegory_slug=None):
    template = 'mainapp/product_detail.html'
    context = {
        'category': get_object_or_404(CategoryModel, slug=category_slug),
        'collection':get_object_or_404(CollectionModel, slug=collection_slug),
        'product': get_object_or_404(ProductModel, slug=product_slug),
    }
    context = make_context(context)
    return render(request, template, context)


def product_detail_sub(request, category_slug, subcategory_slug, collection_slug, product_slug):
    template = 'mainapp/product_detail.html'
    context = {
        'category': get_object_or_404(CategoryModel, slug=category_slug),
        'collection': get_object_or_404(CollectionModel, slug=collection_slug),
        'subcategory': get_object_or_404(SubcategoryModel, slug=subcategory_slug),
        'product': get_object_or_404(ProductModel, slug=product_slug),
    }
    context = make_context(context)
    return render(request, template, context)
