from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'bio']

        widgets = {
            'bio': forms.TextInput(
                attrs={
                    'class': 'form_info'
                }
            )
        }

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','Book', 'content', 'image']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form_info',
                    'placeholder': "post's title"
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'class': 'form_info',
                    'placeholder': "content"
                }
            ),
            'Book': forms.Select(
                attrs={
                    'class': 'form_select',
                }
            )


        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author','title', 'genre', 'image', 'summary']

        widgets = {
            'title':forms.TextInput(
                attrs={
                    'class': 'form_info',
                    'placeholder' : 'Enter book title...'
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form_info',
                    'placeholder': "Author's name"
                }
            ),

            'summary': forms.TextInput(
                attrs={
                    'class': 'form_info',
                    'placeholder': 'A summary of the book'
                }
            ),

            'genre': forms.Select(
                attrs={
                    'class': 'form_select'
                }
            )
        }


class BookClubForm(ModelForm):
    class Meta:
        model = BookClub
        fields = ['name', 'description', 'current_book']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form_info',
                    'placeholder': 'Bookclub name'
                }
            ),

            'description': forms.TextInput(
                attrs={
                    'class': 'form_info',
                    'placeholder': 'Club description...'
                }
            ),
            'current_book': forms.Select(
                attrs={
                    'class': 'form_select'
                }
            )

        }