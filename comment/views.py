from django.http import HttpResponse
from django.shortcuts import render, redirect

from comment.forms import NewComment
from comment.models import Comment
from duck_hacks_2018.util.authority_decorators import *
from ideas.models import Idea, Topic


@logged_in
@ajax
def comment(request):
    cmt = NewComment(request.GET)
    if cmt.is_valid():
        account_id = request.session['user'].id
        news_id = cmt.cleaned_data['news_id']
        news = Idea.get_idea(news_id, 1)[0]
        if not news.has_comment:
            return HttpResponse('failed')
        content = cmt.cleaned_data['content']
        Comment.comment(news_id, account_id, content)
        return HttpResponse('succeed')
    else:
        return HttpResponse('failed')


def get_comment(request, news_id):
    news = Idea.get_idea(news_id, 1)
    if news is None:
        raise Http404()
    if not news[0].has_comment:
        raise Http404()
    page = request.GET.get('page')
    if page is None:
        page = 1
    comments = Comment.get_comment_by_news_id(news_id, page, 1)
    context = comments
    return render(request, 'comments.html', context)