from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('error')
    return render(request, 'front/login.html')


def log_out(request):
    logout(request)
    return redirect('index')