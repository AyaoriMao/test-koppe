from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import * # 追加

from django.contrib.auth.views import LoginView
from .forms import * 

# TemplateViewを継承したクラスを作成
class Lp(generic.TemplateView):
    template_name = 'amazon/lp.html'
    def get_context_data(self, **kwargs):
        context = super(Lp, self).get_context_data(**kwargs)
        all_items = Product.objects.all()
        context['items'] = all_items
        return context

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

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'amazon/login.html'
