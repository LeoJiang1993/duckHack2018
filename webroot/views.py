# Create your views here.
from django.shortcuts import render

from ideas import buz as idea_buz


def index(request, info=None):
    context = dict(info=info)
    return render(request, "index.html", context)


def header(request):
    return render(request, "header.html")


def page_not_found(request):
    return render(request, '404.html')
