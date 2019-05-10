from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as django_auth_views # 追加

app_name = 'amazon'

urlpatterns = [
    path('lp/', views.Lp.as_view(), name='lp'),
    path('items/', views.ItemList.as_view(), name = 'item_list'), # 追加
     path('item/<int:pk>', views.ItemDetail.as_view(), name = 'item_detail'), # 追加
     path('', views.Login.as_view(), name = "login"), # 追加
    path('logout', django_auth_views.LogoutView.as_view(), name = "logout"), # 追加
]
