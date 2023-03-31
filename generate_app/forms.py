from django import forms
from django.contrib.auth.models import User
from .models import PassWord, Account

class PassWordForm(forms.ModelForm):
      class Meta:
            model = PassWord
            fields = {'url', 'passWord', 'service_name'}


class AccountForm(forms.ModelForm):
      password = forms.CharField(widget=forms.PasswordInput(), label='パスワード')

      class Meta():
            model = User
            fields = ('username', 'email', 'password')
            labels = {'username':"ユーザID", 'email':"メール"}


class AddAccountForm(forms.ModelForm):
      class Meta():
            model = Account
            fields = ('last_name', 'first_name', 'account_image',)
            labels = {'last_name': "苗字", 'first_name': "名前", 'account_image': "写真アップロード",}