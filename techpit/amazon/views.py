from django.shortcuts import render
from django.contrib.auth.views import (LoginView, TemplateView, LogoutView)
from django.views.generic import ListView, DetailView
from .forms import (LoginForm,)
from .models import *

# Create your views here.
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'amazon/login.html'

class Lp(TemplateView):
    template_name = 'amazon/lp.html'

class ItemList(ListView):
    model = Product
    template_name = 'amazon/item_list.html'

class ItemDetail(DetailView):
    model = Product