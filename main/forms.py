
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

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