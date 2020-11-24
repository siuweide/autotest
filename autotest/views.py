from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render



# 用户登录
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        print('user', user)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

# 主页
def home(request):
    return render(request, 'home.html')