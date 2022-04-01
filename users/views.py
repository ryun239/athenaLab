from pydoc import render_doc
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def my_login(request):

    if request.method != "POST":
        print("그냥 페이지만 들어왔다...")
        return render(request, 'users/login.html')
    elif request.method == "POST":
        user_name = request.POST["username"]
        user_passwd = request.POST["password"]
        user_lastname = request.POST["lastname"]
        user_fristname = request.POST["firstname"]
        user_student_id = request.POST["student_id"]

        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user = User.objects.create_user(user_name, "", user_passwd)
        user.save()

        
        return HttpResponse("로그인에 성공 했습니다.")
    

def my_signup(request):
    return render(request, 'users/signup.html')
