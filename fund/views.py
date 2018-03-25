from django.shortcuts import render, HttpResponse
from duck_hacks_2018.util.authority_decorators import *
from fund import buz
from fund.forms import MakeFund


@logged_in
def make_fund(request):
    if request.method == "POST":
        form = MakeFund(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            user = request.session['user'].id
            idea = form['idea_id']
            amount = form['amount']
            comment = form['comment']
            buz.fund(user_id=user, idea_id=idea, amount=amount, comment=comment)
            return HttpResponse('Succeed')
        return HttpResponse('failed')
    return render(request, 'make_fund.html', {'idea_id': request.GET['idea_id']})


def get_fund_by_fonder(request, user_id=None):
    if user_id is None:
        user_id = request.session.get('user')
        if user_id is not None:
            user_id = user_id.id
        else:
            raise Http404()
    funds = buz.get_fund_by_fonder(user_id)
    return render(request, 'user_funds.html', {'funds': funds, 'user_id': user_id})


def get_fund_by_idea(request, idea_id):
    return buz.get_fund_by_idea(idea_id)
