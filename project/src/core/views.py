from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView


def index(request):
    return render(request, 'main_page.html')


class Login(LoginView):
    template_name = 'core/login.html'


class Logout(LogoutView):
    template_name = 'core/logout.html'
