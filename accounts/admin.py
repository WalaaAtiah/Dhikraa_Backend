from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "birthday",
        "phone_number",
        "location"

    ]
    add_fieldsets=((
            'None',{
                'fields':('username','email','password1','password2'),
            }
        ),(
            'personal information',{
                'fields':('first_name','last_name',"phone_number","birthday","location"),
            }
        ),)




admin.site.register(CustomUser, CustomUserAdmin)



