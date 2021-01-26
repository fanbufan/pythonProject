from django.shortcuts import HttpResponse, render, redirect
from cmdb import models


# Create your views here.
def index(request):
    data = models.UserInfo.objects.all()
    return render(request, 'index.html', {'user_list': data})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        if username and password:
            if models.UserInfo.objects.filter(username=username, password=password).exists():
                return index(request)
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'msg': '用户名或密码不能为空'})


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        if username and password:
            if models.UserInfo.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'msg': '用户名已存在'})
            else:
                models.UserInfo.objects.create(username=username, password=password)
                return index(request)
        else:
            return render(request, 'signup.html', {'msg': '用户名或密码不能为空'})
