from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import comment
from django.contrib.auth import authenticate, login, logout
from .models import Book, BookClub,  Post, Profile, Comment
from .forms import *
from django.db.models import Q


# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    genre = request.GET.get('genre', '')

    posts = Post.objects.filter(
        Q(Book__title__icontains=q) |
        Q(title__icontains=q) |
        Q(content__icontains=q),
        Book__valid=True
    )

    if genre:
        posts = posts.filter(Book__genre=genre)

    books = Book.objects.filter(valid=True)
    bookclubs = BookClub.objects.all()
    post_comments = Comment.objects.filter(
        Q(post__Book__title__icontains=q)
    )
    genre_choices = Book.GENRE_CHOICES

    context = {'posts': posts,
               'books': books,
               'bookclubs': bookclubs,
               'post_comments': post_comments,
               'genre_choices': genre_choices,
               'selected_genre': genre,
               'current_q': q,
    }
    return render(request, "home.html", context)


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    posts = profile.post_set.all()
    post_comments = profile.comment_set.all()
    books = Book.objects.filter(post__author=profile, valid=True)
    bookclubs = BookClub.objects.all()
    context = {'profile': profile, 'posts': posts, 'post_comments': post_comments, 'books': books, 'bookclubs': bookclubs}
    return render(request, "profile.html", context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=pk)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        comment = Comment.objects.create(
            author=request.user.profile,
            post=post,
            content=request.POST.get('content'),
        )
        return redirect('post', pk=post.id)
    context = {'post': post, 'comments': comments}
    return render(request, "main/post.html", context)


def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'main/post_form.html', context )


def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.user != post.author.user:
        return HttpResponse("You are not the author... ")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,'main/post_form.html', context)


def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.user != post.author.user:
        return HttpResponse("You are not the author... ")

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {'post': post}

    return render(request,'main/post_form.html', context)


def book(request, pk):
    book = Book.objects.get(id=pk)
    context = {'book': book}
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
    form = BookClubForm
    if request.method == 'POST':
        form = BookClubForm(request.POST, request.FILES)
        if form.is_valid():
            club = form.save(commit=False)
            club.host = request.user.profile
            club.save()
            club.members.add(request.user.profile)
            return redirect('home')

    context = {'form': form}
    return render(request,'main/post_form.html', context)


def updateBookClub(request, pk):
    bookClub = BookClub.objects.get(id=pk)
    form = BookClubForm(instance=bookClub)

    if request.method == 'POST':
        form = BookClubForm(request.POST, request.FILES, instance=bookClub)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,'main/post_form.html', context)


def deleteBookClub(request, pk):
    pass


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.info(request, 'Username does not exist')
            return redirect('home')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {'page': page}
    return render(request, 'login_register.html', context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occured during registration")

    context = {'form': form}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request, 'about.html')


