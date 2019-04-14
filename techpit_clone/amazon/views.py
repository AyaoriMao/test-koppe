from django.shortcuts import render
from django.views import generic
from .models import * 
from django.contrib.auth.views import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

# TemplateViewを継承したクラスを作成
class Lp(generic.TemplateView):
    template_name = 'amazon/lp.html'

class ItemList(generic.ListView):
    model = Product
    template_name = 'amazon/item_list.html'
    def get_queryset(self):
        products = Product.objects.all()
        if 'q' in self.request.GET and self.request.GET['q'] != None:
            q = self.request.GET['q']
            products = products.filter(name__icontains = q)

        return products

class ItemDetail(generic.DetailView):
    model = Product
    template_name = 'amazon/item_detail.html'

class Login(LoginView): # 追加
    """ログインページ"""
    form_class = LoginForm
    template_name = 'amazon/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'amazon/lp.html'
