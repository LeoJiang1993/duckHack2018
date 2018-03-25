from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.forms import ModifyAccount, CreateAccount
from account.models import Account
from account.util.send_confirmation_email import send_confirmation_email
from duck_hacks_2018.util.authority_decorators import *

# Create your views here.
from account.util.send_password_reset_email import send_password_reset_email
from webroot.views import index
from account.util import account_info_format


def sign_up(request):
    return render(request, "sign_up.html")


@ajax
@post
def create_account(request):
    form = CreateAccount(request.POST, request.FILES)
    context = {}
    if form.is_valid():
        user_name = form.cleaned_data['user_name']
        password = form.cleaned_data['password']
        if not account_info_format.check_password_format(password):
            context['password'] = 'Error'
        nick_name = form.cleaned_data['nick_name']
        photo = form.cleaned_data['photo']
        email = form.cleaned_data['email']
        email.lower()
        if account_info_format.check_email_format(email):
            context['email'] = 'Error'
        last_name = form.cleaned_data['last_name']
        first_name = form.cleaned_data['first_name']
        if context != {}:
            return HttpResponse(context)
        user = Account.create_account(user_name, password, nick_name, photo, email, last_name, first_name)
        request.session['user'] = user
        if request.session['user'] is not None:
            context = 'succeed'
        else:
            context = 'failed'
    else:
        context = 'failed'
    return HttpResponse(context)


def sign_in(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    request.session['user'] = Account.sign_in(user_name, password)
    if request.session['user'] is not None:
        rt = "succeed"
    else:
        rt = "failed"
    return HttpResponse(rt)


def log_out(request):
    if request.session.get('user') is not None:
        del request.session["user"]
        return HttpResponse("True")
    else:
        return HttpResponse("False")


@logged_in
def modify(request):
    if request.method == 'POST':
        user = request.session['user']
        if user is None:
            raise Http404()
        form = ModifyAccount(request.POST, request.FILES)
        if form.is_valid():
            user = Account.modify_account(user.id, form.cleaned_data['nick_name'], form.cleaned_data['photo'],
                                          form.cleaned_data['first_name'], form.cleaned_data['last_name'])
        request.session['user'] = user
    return render(request, 'modify_account.html')