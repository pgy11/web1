from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserInfo
from django.template import loader

# Create your views here.
INIT = '0'
SUCCESS = '1'
FAIL = '2'

def index(request):
    context = {'stat': INIT}
    return render(request, 'polls/index.html', context)

def login(request):
    context = {'msg': ''}
    return render(request, 'polls/login.html', context=context)

def signin(request):
    email = request.POST['email']
    pw = request.POST['password']

    try:
        user = UserInfo.objects.get(email=email)
        if user.password == pw:
            context = {'stat': SUCCESS, 'name': user.firstname, 'email': user.email}
            return render(request, 'polls/index.html', context)

        else:
            context = {'msg': '이메일 또는 비밀번호를 올바르게 입력하세요.'} 
            return render(request, 'polls/login.html', context=context)

    except:
        context = {'msg': '이메일 또는 비밀번호를 올바르게 입력하세요.'} 
        return render(request, 'polls/login.html', context=context)

def signup(request):  
    return render(request, 'polls/signup.html')

def checkmail(request):
    email = request.POST['email']
    try:
        _ = UserInfo.objects.get(email=email)
        return render(request, 'polls/signup.html',{'msg': 'not available'})
    except:
        return render(request, 'polls/signup.html',{'msg': 'available'})

def signout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def reqmember(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    pw = request.POST['password']
    address = request.POST['address']

    newuser = UserInfo(firstname=firstname, lastname=lastname, email=email,
     password=pw, address=address)
    newuser.save()

    return HttpResponseRedirect(reverse('index'))

def updateinfo(request):
    email = request.GET['email']
    firstname = request.GET['firstname']
    user = UserInfo.objects.get(email=email)
    context = {
        'email': email,
        'firstname': firstname,
        'lastname': user.lastname,
        'address': user.address
    }
    return render(request, 'polls/updateinfo.html', context=context)

def requpdate(request):
    email = request.POST['email']
    firstname = request.POST['firstname'].rstrip()
    lastname = request.POST['lastname'].rstrip()
    password = request.POST['password'].rstrip()
    address = request.POST['address'].rstrip()
    
    user = UserInfo.objects.get(email=email)

    if firstname: user.firstname = firstname
    if lastname: user.lastname = lastname
    if password: user.password = password
    if address: user.address = address
    user.save()

    context = {'stat': SUCCESS,'name': user.firstname, 'email': user.email}

    return render(request, 'polls/index.html', context=context)

def deleteinfo(request):
    email = request.GET['email']
    firstname = request.GET['firstname']
    context = {'stat': INIT, 'email': email, 'firstname': firstname}
    return render(request, 'polls/deleteinfo.html', context)
    
def reqdelete(request):
    email = request.POST['email']
    pw = request.POST['password']
    firstname = request.POST['firstname']
    user = UserInfo.objects.get(email=email)

    if user.password != pw:
        context = {'stat': FAIL, 'msg': '비밀번호가 틀렸습니다.', 'firstname':firstname, 'email':email}
        return render(request, 'polls/deleteinfo.html', context)
        
    auth.logout(request)
    user.delete()
    context = {'stat': SUCCESS, 'firstname': firstname}
    return render(request, 'polls/deleteinfo.html', context)
