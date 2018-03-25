import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models

# Create your models here.
from account.models import Account
from ideas.storage import NewsImageStorage


class Idea(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Account)
    content = models.CharField(max_length=2000)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    viewed = models.IntegerField(null=0)

    @staticmethod
    def save_idea(_id, title, author, content):
        if _id == 0:
            new_news = Idea(title=title, author_id=author, content=content,
                            viewed=0)
            new_news.save()
            return new_news
        news = Idea.objects.filter(id=_id)
        news.update(title=title, author=author, content=content)
        return news.first()

    @staticmethod
    def get_idea(idea_id):
        return Idea.objects.filter(id=idea_id)

    @staticmethod
    def get_ideas():
        return Idea.objects.all()

    @staticmethod
    def get_idea_list_for_edit(user_id):
        return Idea.objects.filter(author_id=user_id)

    @staticmethod
    def get_idea_for_edit(user_id, idea_id):
        return Idea.objects.get(id=idea_id, author_id=user_id)
