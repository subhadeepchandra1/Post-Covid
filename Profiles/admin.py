from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets
<<<<<<< HEAD
    fieldsets += ('Custom fields set', {'fields': ('employment','timer_active','timer_last_active',
                'social_active','social_count')}),
=======
    fieldsets += ('Custom fields set', {'fields': ('employment','timer_active','timer_last_active')}),
>>>>>>> 1bff0b3c851709a031faa42116d7f8afb8d6269b
    list_display = ['email', 'first_name' ,'last_name','employment']

admin.site.register(CustomUser, CustomUserAdmin)