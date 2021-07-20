from .models import Customer
from django.contrib.auth import models
from django.contrib.auth.forms import (UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
,PasswordResetForm,SetPasswordForm)
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation



class RegisterForm(UserCreationForm):
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=True,label='email',widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    
    password=forms.CharField(label='password',strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    

class PcForm(PasswordChangeForm):
        error_css_class = 'has-error'
        error_messages = {'password_incorrect':
                  "please enter currect password"}
        old_password = forms.CharField(required=True, label='old password',
                      widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'password is not currect'})

        new_password1 = forms.CharField(required=True, label='new password',
                      widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
                        'class': 'form-control'}),
                        help_text=password_validation.password_validators_help_text_html())

        new_password2 = forms.CharField(required=True, label='confirm password',
                      widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
                        'class': 'form-control'}))

class passresetform(PasswordResetForm):
  email=forms.EmailField(required=True,label='Email',max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))

class mysetpasswordform(SetPasswordForm):
        new_password1 = forms.CharField(required=True, label='new password',
                      widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
                        'class': 'form-control'}),
                        help_text=password_validation.password_validators_help_text_html())

        new_password2 = forms.CharField(required=True, label='confirm password',
                      widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
                        'class': 'form-control'}))

class customerprofile(forms.ModelForm):
  class Meta:
    model=Customer
    fields=['name','locality','city','zipcode','state']
    widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}),
    'city':forms.TextInput(attrs={'class':'form-control'}),'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
    'state':forms.Select(attrs={'class':'form-control'})}