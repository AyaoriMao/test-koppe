from django.contrib import admin
from django.urls import path
from django.conf.urls import include # 追加
from django.conf import settings # 追加

urlpatterns = [
    path('techpit/admin/', admin.site.urls),
    path('techpit/amazon/', include('amazon.urls')) # 追加
]
