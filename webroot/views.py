# Create your views here.
from django.shortcuts import render

from ideas import buz as idea_buz

def index(request, info=None):
    context = dict(info=info)
    return render(request, "index.html", context)


def header(request):
    topics = idea_buz.get_topic_list()
    context = dict(topics=topics)
    return render(request, "header.html", context)


def page_not_found(request):
    return render(request, '404.html')
