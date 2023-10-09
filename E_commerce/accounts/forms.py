from typing import Any
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.views.generic.edit import FormMixin


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(
        label='Email Address',
        
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')

    def clean_password(self):
        password1 = self.cleaned_data.get('passowrd1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords don't matchs")
        return password2
    
    def save(self, commit:bool = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

# class FormChangePassword(FormMixin, PasswordChangeForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['old_password'].widget.attrs.update({'class' : 'stext-111 cl2 plh3 size-116 p-lr-18','placeholder':'Old password'})
#         self.fields['new_password1'].widget.attrs.update({'class' : 'stext-111 cl2 plh3 size-116 p-lr-18','placeholder':'new password'})
#         self.fields['new_password2'].widget.attrs.update({'class' : 'stext-111 cl2 plh3 size-116 p-lr-18','placeholder':'confirm password'})
class FormChangePassword(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True, 
                   'placeholder': 'Old Password'}),
    )
    new_password1 = forms.CharField(
        label='New Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'placeholder': 'New Password'}),

        # help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label='Confirm Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'placeholder': 'Confirm password'}),
    )

    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password1', 'new_password2']

    # def clean(self):
    #     old_password = self.cleaned_data.get['old_password']
    #     new_password1 = self.cleaned_data.get['new_password1']
    #     new_password2 = self.cleaned_data.get['new_password2']

    #     if new_password1 and new_password2 and new_password1 != new_password1:
    #         raise ValueError("The two password fields did not match")
    #     return new_password2

    # def pri(self):
    #     print(self.clean())

    # def save(self, commit=False):
    #     password = self.clean()
    #     self.user.set_password(password)
    #     if commit:
    #         self.user.save()
    #     return self.user
