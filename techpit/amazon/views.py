from django.shortcuts import render

from django.contrib.auth.views import (LoginView, TemplateView, LogoutView)
from .forms import (LoginForm,)

# Create your views here.
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'amazon/login.html'

class Lp(TemplateView):
    template_name = 'amazon/lp.html'
