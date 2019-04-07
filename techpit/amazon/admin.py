from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.contrib.admin.utils import quote
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import *


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)



class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )   
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'name', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active')
    search_fields = ('email','name')
    ordering = ('email',)

class MyShoppingCartAdmin(admin.ModelAdmin):
    model = ShoppingCart
    list_display = ('user',)

admin.site.register(User, MyUserAdmin)
admin.site.register(ShoppingCart, MyShoppingCartAdmin)
