from django.shortcuts import render

# djangoの汎用クラスビューのパッケージをインポート
from django.views import generic

# TemplateViewを継承したクラスを作成
class Lp(generic.TemplateView):
    template_name = 'amazon/lp.html'

