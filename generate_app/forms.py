from django import forms

from .models import PassWord

class PassWordForm(forms.ModelForm):
      class Meta:
            model = PassWord
            fields = {'url', 'passWord', 'service_name'}