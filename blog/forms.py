from django import forms
from django.forms import fields, widgets
from .models import AuthorRegister, Post


class signupAuthor(forms.ModelForm):
    class Meta:
        model = AuthorRegister
        fields =  '__all__'
        # labels = {
        #     'first_name' : 'First Name',
        #     'last_name' : 'Last Name',
        #     'email' : 'Email',
        #     'username' : 'Username',
        # }

        # adding bootstrap class as widget attrs, to make form look good
        # widgets = {
        #     'username' : forms.TextInput(attrs={'class' : 'form-control my-1'}),
        #     'first_name' : forms.TextInput(attrs={'class' : 'form-control my-1'}),
        #     'last_name' : forms.TextInput(attrs={'class' : 'form-control my-1'}),
        #     'email' : forms.EmailInput(attrs={'class' : 'form-control my-1'}),
        # }

class Postfm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        