from django.shortcuts import render
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
    return context


def index(request):
    template = 'mainapp/index.html'
    context = {
        'indexpage': IndexPageModel.objects.first(),
        'slides': IndexPageSlideModel.objects.all(),
        'products': IndexPageProductModel.objects.all(),
        'faqs': IndexPageFAQModel.objects.all(),
        'team': IndexPageTeamUnitModel.objects.all(),
        'reviews': ReviewModel.objects.all(),
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
