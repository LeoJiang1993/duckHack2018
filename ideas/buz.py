from duck_hacks_2018.util.authority_decorators import *
from ideas.models import *


def get_idea_for_edit(user_id, idea_id):
    idea = Idea.get_idea_for_edit(user_id, idea_id)
    if idea is None:
        raise Http404()
    return idea


def get_idea_list_for_edit(user_id):
    return Idea.get_idea_list_for_edit(user_id)


def get_idea(idea_id):
    return Idea.get_idea(idea_id)


def get_ideas():
    return Idea.get_ideas()


def save_idea(id, title, author_id, content):
    return Idea.save_idea(id, title, author_id, content)