import email
from pydoc import render_doc
import re
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from .models import User as my_user

# Create your views here.

def my_index(request):
    # return render(request, 'users/login.html')
    print("리다이렉트")
    
    return render(request, 'users/index.html')


def my_logout(request):
    if request.method == 'POST':            
        logout(request)
    print("Logout !!")
    return render(request, 'users/index.html')

def my_login(request):

    print(request.POST)

    if request.method != "POST":
        print("그냥 페이지만 들어왔다...")
        return render(request, 'users/login.html')
    elif request.method == "POST":
        user_email = request.POST["email"]
        user_passwd = request.POST["password"]

        user = authenticate(email=user_email, password=user_passwd)

        if user is not None:
            print('와우 로그인!!!')
        else:
            print('아... 로그인 실패...')
        
        return render(request, 'users/index.html', {'user':user})

def my_signup(request):

    if request.method != "POST":
        return render(request, 'users/signup.html')
    else:
        user_email = request.POST["email"]
        user_birth_of_date = request.POST["birth_of_date"]
        user_passwd0 = request.POST["password0"]
        user_passwd1 = request.POST["password1"]

        if user_email is None and user_passwd0 != user_passwd1:
            return HttpResponse("아이디 또는 비번이 틀립니다.")
        else:
            new_user = my_user.objects.create_user(email=user_email, date_of_birth = user_birth_of_date, password = user_passwd0)
            
            if new_user is None:
                print("회원가입 실패...")
                return HttpResponse("회원가입 실패...")
            else:
                print("회원가입 성공!!")
                return HttpResponse("회원가입 성고!!")


