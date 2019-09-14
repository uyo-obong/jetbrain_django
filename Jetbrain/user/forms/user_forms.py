from django import forms
from django.contrib.auth.models import User
from Jetbrain.user.models import Profile


class SignUp(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}), label='')
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password'}), label='')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class UpdateUser(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']