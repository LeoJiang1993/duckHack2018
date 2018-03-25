from django.http import HttpResponse
from django.shortcuts import render, redirect

from duck_hacks_2018.util.authority_decorators import *
from favourite import buz


@logged_in
def like(request, idea_id):
    user = request.session['user']
    buz.like(user_id=user.id, idea_id=idea_id)
    return redirect('/idea/' + idea_id)


@logged_in
def unlike(request, idea_id):
    user = request.session['user']
    buz.unlike(user_id=user.id, idea_id=idea_id)
    return redirect('/idea/' + idea_id)


@logged_in
def get_list(request):
    user = request.session['user']
    favourite_list = buz.get_favourite(user.id)
    return render(request, 'favourite_list.html', {'favourite_list': favourite_list})


def bar(request, idea_id):
    user = request.session.get('user')
    liked = buz.get_liked(idea_id)
    if user is None:
        is_liked = False
    else:
        user = user.id
        is_liked = buz.is_like(user, idea_id)
    return render(request, 'favourite_bar.html', {'idea_id': idea_id, 'liked': liked, 'is_liked': is_liked})
