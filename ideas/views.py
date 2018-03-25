from django.shortcuts import render

from ideas import buz
from ideas.forms import *
from duck_hacks_2018.util.authority_decorators import *


def idea_content(request, idea_id):
    idea = buz.get_idea(idea_id)
    if idea.count() == 0:
        raise Http404()
    context = dict(idea=idea[0])
    return render(request, "idea.html", context)


def idea_content_c(request, idea_id):
    idea = buz.get_idea(idea_id)
    if idea.count() == 0:
        raise Http404()
    viewed = idea[0].viewed
    idea.update(viewed=viewed + 1)
    context = dict(news_context=idea.first())
    return render(request, "idea_content.html", context)


def idea_list(request):
    ideas = buz.get_ideas()
    context = dict(ideas=ideas)
    return render(request, "idea_list.html", context)


@logged_in
def idea_list_for_edit(request):
    user = request.session["user"]
    context = {'ideas': buz.get_idea_list_for_edit(user)}
    return render(request, 'my_ideas.html', context)


@logged_in
def edit_idea(request, idea_id):
    user = request.session.get('user')
    context= {'idea': buz.get_idea_for_edit(user_id=user.id, idea_id=idea_id)}
    return render(request, 'edit_idea.html', context)


@logged_in
def new_idea(request):
    return render(request, 'edit_idea.html')


@logged_in
def save_idea(request):
    form = IdeaEdit(request.POST)
    if form.is_valid():
        news = form.cleaned_data
        idea = buz.save_idea(author_id=request.session['user'].id, id=news['id'],
                             title=news['title'], content=news['content'])
        return edit_idea(request, idea.id)
