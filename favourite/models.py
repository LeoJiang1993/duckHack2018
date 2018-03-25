import json

from django.db import models

# Create your models here.
from account.models import Account
from ideas.models import Idea


class Favourite(models.Model):
    account = models.ForeignKey(Account)
    idea = models.ForeignKey(Idea)

    @staticmethod
    def add_favourite(user_id, idea_id):
        favourite = Favourite(account_id=user_id, idea_id=idea_id)
        favourite.save()
        return True

    @staticmethod
    def remove_favourite(user_id, idea_id):
        item = Favourite.objects.filter(account_id=user_id, idea_id=idea_id)
        if item is None:
            return False
        item.delete()
        return True

    @staticmethod
    def get_favourite(user_id):
        return Favourite.objects.filter(account_id=user_id)

    @staticmethod
    def get_liked(idea_id):
        return Favourite.objects.filter(idea_id=idea_id).count()

    @staticmethod
    def is_like(user_id, idea_id):
        return Favourite.objects.filter(account_id=user_id, idea_id=idea_id).count() == 1
