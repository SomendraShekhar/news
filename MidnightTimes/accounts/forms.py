from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class CustomLoginView(LoginView):
    template_name = 'custom_login.html'
