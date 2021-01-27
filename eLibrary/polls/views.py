from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from .models import UserInfo, Book

# Create your views here.
INIT = '0'
SUCCESS = '1'
FAIL = '2'
books = Book.objects.all()

def index(request):
    context = {'books': books}
    return render(request, 'polls/index.html', context)

def login(request):
    context = {'msg': ''}
    return render(request, 'polls/login.html', context=context)

def signin(request):
    if 'email' in request.session.keys():
        return HttpResponseRedirect(reverse('index'))

    email = request.POST['email']
    pw = request.POST['password']
    try:
        user = UserInfo.objects.get(email=email)
        if user.password == pw:
            request.session['email'] = user.email
            request.session['firstname'] = user.firstname
            return HttpResponseRedirect(reverse('index'))
        
        else: 
            return render(request, 'polls/login.html', {'msg': 'ID 또는 비밀번호가 틀렸습니다.'})

    except:
        return render(request, 'polls/login.html', {'msg': 'ID 또는 비밀번호가 틀렸습니다.'})
    

def signup(request):
    return render(request, 'polls/signup.html')

def signout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def reqmember(request):

    msg = check_signup(request)
    if msg != 'valid':
        messages.add_message(request, messages.ERROR, msg)
        return render(request, 'polls/signup.html')

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    pw = request.POST['password']
    address = request.POST['address']
    phonenumber = request.POST['phonenumber']

    newuser = UserInfo(firstname=firstname, lastname=lastname, email=email,
    password=pw, address=address, phonenumber=phonenumber)
    newuser.save()

    messages.add_message(request, messages.SUCCESS, '회원가입에 성공하였습니다.')
    return render(request, 'polls/signup.html')
    

def searchmem(request):
    return render(request, 'polls/searchmem.html')

def retrievemem(request):
    phonenumber = request.POST['phonenumber']
    try:
        user = UserInfo.objects.get(phonenumber=phonenumber)
        messages.add_message(request, messages.SUCCESS, 'success')
        context = {'usermail': user.email, 'password': user.password}
        return render(request, 'polls/searchmem.html', context)
    
    except:
        messages.add_message(request, messages.ERROR, '없는 전화번호입니다.')
        return render(request, 'polls/searchmem.html')
    
        
def updateinfo(request):
    if 'email' not in request.session.keys():
        return HttpResponseRedirect(reverse('login'))

    email = request.GET['email']
    firstname = request.GET['firstname']
    try:
        user = UserInfo.objects.get(email=email)
        context = {
            'usermail': email,
            'firstname': firstname,
            'lastname': user.lastname,
            'address': user.address
        }
        return render(request, 'polls/updateinfo.html', context=context)
    
    except:
        return HttpResponseRedirect(reverse('index'))

def requpdate(request):
    if 'email' not in request.session.keys():
        return HttpResponseRedirect(reverse('login'))

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

    return HttpResponseRedirect(reverse('index'))

def deleteinfo(request):
    if 'email' not in request.session.keys():
        return HttpResponseRedirect(reverse('login'))

    email = request.GET['email']
    firstname = request.GET['firstname']
    context = {'stat': INIT, 'usermail': email, 'firstname': firstname}
    return render(request, 'polls/deleteinfo.html', context)
    
def reqdelete(request):
    if 'email' not in request.session.keys():
        return HttpResponseRedirect(reverse('login'))

    email = request.POST['email']
    pw = request.POST['password']
    firstname = request.POST['firstname']
    user = UserInfo.objects.get(email=email)

    if user.password != pw:
        context = {'stat': FAIL, 'msg': '비밀번호가 틀렸습니다.', 'firstname':firstname, 'usermail':email}
        return render(request, 'polls/deleteinfo.html', context)
          
    auth.logout(request)
    user.delete()
    context = {'stat': SUCCESS, 'firstname': firstname}
    return render(request, 'polls/deleteinfo.html', context)

def bookinfo(request):
    if 'email' not in request.session.keys():
        return HttpResponseRedirect(reverse('login'))

    imgurl = request.GET['imgurl']
    try:
        book = Book.objects.get(image_URL=imgurl)
        return render(request, 'polls/bookinfo.html', context={'book': book})
    except:
        pass


def check_signup(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    pw = request.POST['password']
    cpw = request.POST['cpassword']
    address = request.POST['address']
    phonenumber = request.POST['phonenumber']

    if not firstname or not lastname: return '이름을 입력하세요'
    if not email: return '이메일을 입력하세요'
    if not pw: return '비밀번호를 입력하세요'
    if pw != cpw: return '비밀번호가 서로 맞지 않습니다.'
    if not address: return '주소를 입력하세요.'
    if '@' not in email: return '이메일 형식이 올바르지 않습니다.'
    if not phonenumber: return '전화번호를 입력하세요.'
    if '-' in phonenumber: return '-없이 전화번호를 입력하세요.'
    if not str.isdigit(phonenumber): return '숫자를 입력하세요'

    try:
        _ = UserInfo.objects.get(email=email)
        return '이미 존재하는 이메일입니다.'
    except:
        return 'valid'
