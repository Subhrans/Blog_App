from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile,Post,Category

choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class SignUp(UserCreationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Password (again)", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','password1','password2']

    def save(self, commit=True):
        user = super(SignUp, self).save(commit=False)
        first_name = user.username.split('@')
        user.first_name = first_name[0]
        user.email = user.username
        user.save()
        return user

class Login(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','password']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','description','image']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'description':forms.Textarea(attrs={'class':'form-control'}),
                   'category':forms.Select(choices=choice_list,attrs={'class':'form-control',
                                                                      'placeholder':'select category'}),
                   'image':forms.FileInput(attrs={'class':'form-control-file'}),
                   }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_Image','cover_Image','bio']

class ChangeProfilePicForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_Image']