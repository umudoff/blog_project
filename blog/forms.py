from django import forms
from blog.models import Post, Comment, UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),
    help_text="Please enter a password.")
    email = forms.CharField(help_text="Please enter your email.",
    error_messages={'invalid': 'User with this e-mail already registred'})
    username = forms.CharField(help_text="Please enter a username.")
    first_name = forms.CharField(help_text="Enter your first name.")
    last_name = forms.CharField(help_text="Enter your last name")
    #is_staff = 0


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile




class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128,help_text="Title of the post")
    body = forms.CharField(widget=forms.Textarea, max_length=999, help_text="Fill the content")
    class Meta:
        model = Post
    
    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
    #     self.fields['body'].widget.attrs['height'] = 100px
    #     self.fields['body'].widget.attrs['width'] = 100px

class CommentForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea, max_length=999, help_text="Add comment")
    
    
    class Meta:
        model=Comment



    
