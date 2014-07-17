from django.http import Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from account.forms import *
from account.models import *
import pdb
pdb.set_trace()

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def login_page(request):
    if request.method == 'POST':
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
    return login(request)

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form':form
        })
    return render_to_response('registration/register.html', variables)

@login_required
def account_page(request):
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            account = Account.objects.create(
                user=user,
                avatar=form.cleaned_data['avatar'],
                introduction=form.cleaned_data['introduction'],
                )
            account.save()
            return HttpResponseRedirect('/user/%s/' % request.user.username)
    else:
    	# first time query, the account model is empty
        try:
            account = Account.objects.get(user_id=request.user.id)
            introduction = account.introduction
        except:
        	introduction = ''
        form = AccountForm({
            'username': request.user.username,
            'introduction': introduction,
            })
    variables = RequestContext(request, {
        'form':form
        })
    return render_to_response('account/account.html', variables)
    