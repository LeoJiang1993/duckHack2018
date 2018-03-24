import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from news.forms import NewsEdit
from news.models import News, NewsTopic, NewsOnSpecialPlace
from duck_hacks_2018.util.authority_decorators import *
from news.util.save_files import save_news_picture


def news(request):
    news = NewsOnSpecialPlace.get_list(4)
    topics = NewsTopic.get_topic_list()
    context = dict(newss=news, topics=topics)
    return render(request, 'top_news.html', context)


def news_content(request, news_id):
    news_object = News.get_news(news_id, 1)
    if news_object.count() == 1:
        context = dict(news_context=news_object.first())
        return render(request, "news.html", context)
    else:
        raise Http404()


def news_content_c(request, news_id):
    news_object = News.get_news(news_id, 1)
    if news_object.count() == 1:
        viewed = news_object[0].viewed
        news_object.update(viewed=viewed + 1)
        context = dict(news_context=news_object.first())
        return render(request, "news_content.html", context)
    else:
        raise Http404()


def news_list(request, news_topic_id):
    news_topic = NewsTopic.get_topic(news_topic_id)
    if news_topic is None:
        raise Http404()
    context = dict(topics=NewsTopic.get_topic_list(), news_topic=news_topic,
                   news_topic_id=news_topic_id)
    return render(request, "news_list.html", context)


def news_list_list(request):
    news_topic_id = request.GET.get('topic_id')
    page = request.GET.get('page')
    if page is None:
        page = 1
    context = News.get_news_list_by_topic(news_topic_id, 1, page)
    return render(request, 'news_list_list.html', context)