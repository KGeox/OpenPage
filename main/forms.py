
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'bio']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author','title', 'genre', 'image', 'summary']


class BookClubForm(ModelForm):
    class Meta:
        model = BookClub
        fields = ['name', 'description', 'current_book']