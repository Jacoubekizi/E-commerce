from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# from django.contrib.auth.context_processors

# Register your models here.

# class UserCreationForm(forms.ModelForm):

#     password1= forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2= forms.CharField(label='password confirmatio', widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ('email',)

#     def clean_password2(self):
#         password1=self.cleaned_data.get('password1')
#         password2=self.cleaned_data.get('password2')
        
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("passwords dont match")
#         return password2
    
#     def save(self, commit: bool = True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         if commit:
#             user.save()
#         return user
    
# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()
#     class Meta:
#         model=CustomUser
#         fields='__all__'

class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    # change_password_form = 

    list_display=('email', 'username',)
    fieldsets = (
    (None, 
         {'fields':('email', 'password',)}
     ),
    ('User Information',
        {'fields':('username', 'first_name', 'last_name')}
    ),
    ('Permissions', 
        {'fields':('is_staff', 'is_superuser', 'is_active', 'groups','user_permissions')}
    ),
    ('Registration', 
        {'fields':('date_joined', 'last_login',)}
    )
    )

    search_fields=('email',)
    ordering=('email',)
    filter_horizontal=()

admin.site.register(CustomUser,UserAdmin)
# admin.site.unregister(Group)