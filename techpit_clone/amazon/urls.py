from django.urls import path
from . import views
from django.contrib import admin

app_name = 'amazon'

urlpatterns = [
    path('lp/', views.Lp.as_view(), name='lp'),
    path('items/', views.ItemList.as_view(), name = 'item_list'),
    path('item/<int:pk>', views.ItemDetail.as_view(), name = 'item_detail'), 
    path('', views.Login.as_view(), name = "login"),
    path('logout', views.Logout.as_view(), name = "logout"),
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
    path('sign_up/done/<token>', views.SignUpDone.as_view(), name='sign_up_done'),
]