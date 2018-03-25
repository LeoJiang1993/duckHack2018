import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models

# Create your models here.
from account.models import Account
from ideas.storage import NewsImageStorage


class Topic(models.Model):
    description = models.CharField(max_length=30)

    @staticmethod
    def get_topic(topic_id):
        return Topic.objects.get(id=topic_id).description

    @staticmethod
    def get_topic_list():
        return Topic.objects.all()

    @staticmethod
    def add_topic(description):
        topic = Topic(description=str(description))
        topic.save()
        return topic


class Idea(models.Model):
    IDEA_STATUS = (
        (1, u'Online'),
        (2, u'Draft'),
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=IDEA_STATUS)
    topic = models.ForeignKey(Topic)
    viewed = models.IntegerField(null=0)

    @staticmethod
    def save_idea(_id, title, author, content, status, topic, has_comment):
        if _id == 0:
            new_news = Idea(title=title, author=author, content=content, status=status,
                            topic_id=topic, viewed=0, has_comment=has_comment)
            new_news.save()
            return new_news
        news = Idea.objects.filter(id=_id)
        news.update(title=title, author=author, content=content, status=status, topic_id=topic)
        return news.first()

    @staticmethod
    def get_idea(idea_id):
        return Idea.objects.filter(id=idea_id)

    @staticmethod
    def get_idea_by_topic(topic):
        newses = Idea.objects.filter(status=status, topic_id=topic).order_by('time_modified').reverse()
        if newses.count() == 0:
            rt = dict(newses=None, pages=0, page=0)
            return rt
        if page == -1:
            return dict(newses=newses)
        pager = Paginator(newses, 20)
        try:
            newses = pager.page(page)
        except PageNotAnInteger:
            newses = pager.page(1)
            page = 1
        except EmptyPage:
            newses = pager.page(pager.num_pages)
            page = pager.num_pages
        return dict(newses=newses, pages=pager.num_pages, page=int(page))

    @staticmethod
    def get_idea_list_for_edit(user_id):
        return Idea.objects.filter(user_id=user_id)

    @staticmethod
    def get_idea_for_edit(user_id, idea_id):
        return Idea.objects.get(id=idea_id, user_id=user_id)
