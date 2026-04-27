from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import comment
from django.contrib.auth import authenticate, login, logout
from main.models import Book, BookClub,  Post, Profile, Comment
from .forms import *

# Create your views here.

def home(request):
    posts = Post.objects.all()
    books = Book.objects.all()


    context = {'posts': posts, 'books': books}
    return render(request, "home.html", context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    posts = profile.posts_set.all()
    books = profile.books_set.all()
    comments = profile.comments_set.all()
    context = {'profile': profile, 'posts': posts, 'books': books, 'comments': comments}
    return render(request, "profile.html", context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=pk)

    context = {'post': post, 'comments': comments}
    return render(request, "main/post.html", context)

def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'main/post_form.html', context )

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,'main/post_form.html', context)

def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {'post': post}

    return render(request,'main/post_form.html', context)

def book(request, pk):
    book = Book.objects.get(id=pk)
    posts = book.posts_set.all()
    context = {'book': book, 'posts': posts}
    return render(request, 'main/book.html', context)

def createBook(request):
    form = BookForm
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'main/post_form.html', context)

def bookclub(request, pk):
    bookclub = BookClub.objects.get(id=pk)
    context = {'bookclub': bookclub}
    return render(request,'main/bookclub.html', context)

def createBookClub(request):
    pass

def loginPage(request):
    return HttpResponse("Hello Login")

def about(request):
    return render(request, 'about.html')


