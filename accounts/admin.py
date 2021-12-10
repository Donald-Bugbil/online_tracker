from django.contrib import admin
from . import models 
from django.contrib.auth.admin import UserAdmin
from . import forms


# Register your models here.

class customUserAdmin(UserAdmin):
    add_form = forms.customUserCreationForm
    form = forms.customUserChangeForm
    model = models.customUserModel
    list_display = ['email', 'username']


admin.site.register(models.customUserModel, customUserAdmin)
