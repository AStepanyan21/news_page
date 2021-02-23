from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import News, Categories


def news_page(request):
    news_list = News.objects.order_by('-pub_date')[:10]
    categories_list = Categories.objects.all()
    template = loader.get_template('news/index.html')
    context = {
        'news_list': news_list,
        'categories_list': categories_list
    }
    return HttpResponse(template.render(context, request))


def categories_page(request, categories_name):
    categories = categories_name
    news_list_by_categories = News.objects.filter(categories__name=categories_name)
    news_list_by_sub_categories = News.objects.filter(sub_categories__name=categories_name)
    return render(request, 'news/categories.html',
                  {'news_list_by_categories': news_list_by_categories,
                   'news_list_by_sub_categories': news_list_by_sub_categories,
                   'categories': categories})


def detail_page(request, news_id):
    news = News.objects.get(pk=news_id)
    categories = news.sub_categories.all()
    return render(request, 'news/details.html', {
        'news': news,
        'categories': categories
    })
