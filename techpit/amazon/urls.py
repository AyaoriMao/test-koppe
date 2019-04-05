
from django.urls import path
from . import views

app_name = "amazon"
urlpatterns = [
    path('', views.Login.as_view(), name = "login"),
    path('lp/', views.Lp.as_view(), name = 'lp')
]

