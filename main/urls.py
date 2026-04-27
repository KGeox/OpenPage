from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),

    path('profile/<str:pk>/',views.profile,name='profile'),

    path('post/<str:pk>/',views.post,name='post'),

    path('book/<str:pk>/',views.book,name='book'),

    path('bookclub/<str:pk>/',views.bookclub,name='bookclub'),

    path('create-book', views.createBook, name='create-Book'),

    path('create-bookclub', views.createBookClub, name='create-BookClub'),

    path('create-post', views.createPost, name='create-Post'),

    path('update-post', views.updatePost, name='update-Post'),

    path('delete-post', views.deletePost, name='delete-Post'),

    # path('update-bookclub', views.updateBookClub, name='update-BookClub'),

    path('delete-bookclub', views.deleteBookClub, name='delete-BookClub'),

    path('about',views.about,name='about'),

]