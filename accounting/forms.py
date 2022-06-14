from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class SavePayRecordForm(forms.ModelForm):
     def clean(self):
        payed = self.cleaned_data['request'].payed
        if payed:
            raise forms.ValidationError({'request': "This request is payed before"})