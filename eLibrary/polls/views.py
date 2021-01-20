from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def index(request):
    return render(request, 'polls/index.html')


def signin(request):
    print('log', request.POST.keys())
    email = request.POST['email']
    pw = request.POST['password']
    user = auth.authenticate(request, email=email, password=pw)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('index'))
    
    else:
        context = {'msg': '이메일 또는 비밀번호를 올바르게 입력하세요.'} 
        return render(request, 'polls/login.html', context=context)

def signup(request):
    return render(request, 'polls/signup.html')