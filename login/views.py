from django.shortcuts import render

def login(request):
    return render(request, 'login/login.html')

def registration(request):
    return render(request, 'registration/registration.html')