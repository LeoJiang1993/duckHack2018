from duck_hacks_2018.util.authority_decorators import *
from ideas.models import *


@logged_in
def get_idea_for_edit(user_id, idea_id):
    idea = Idea.get_idea_for_edit(user_id, idea_id)
    if idea is None:
        raise Http404()
    return idea


@logged_in
def get_idea_list_for_edit(user_id):
    return Idea.get_idea_list_for_edit(user_id)


def get_idea(idea_id):
    return Idea.get_idea(idea_id)


def get_ideas_by_topic(topic_id):
    return Idea.get_idea_by_topic(topic_id)


def save_idea(id, title, author, content, status, topic, has_comment):
    return Idea.save_idea(id, title, author, content, status, topic, has_comment)


def get_topic(topic_id):
    return Topic.get_topic(topic_id)


def get_topic_list():
    return Topic.get_topic_list()
