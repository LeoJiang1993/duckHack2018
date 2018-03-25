from duck_hacks_2018.util.authority_decorators import *
from favourite.models import Favourite


def get_favourite(user_id):
    return Favourite.get_favourite(user_id=user_id)


def like(user_id, idea_id):
    return Favourite.add_favourite(user_id, idea_id)


def unlike(user_id, idea_id):
    return Favourite.remove_favourite(user_id, idea_id)


def get_liked(idea_id):
    return Favourite.get_liked(idea_id)


def is_like(user_id, idea_id):
    return Favourite.is_like(user_id, idea_id)
