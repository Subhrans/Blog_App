from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile,Post


class SignUp(UserCreationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Password (again)", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','password1','password2']

class Login(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','password']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','image']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'description':forms.TextInput(attrs={'class':'form-control'}),
                   'image':forms.FileInput(attrs={'class':'form-control-file'}),
                   }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_Image','bio']