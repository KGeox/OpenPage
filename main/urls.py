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

    path('update-post/<str:pk>/', views.updatePost, name='update-Post'),

    path('delete-post/<str:pk>/', views.deletePost, name='delete-Post'),

    # path('update-bookclub', views.updateBookClub, name='update-BookClub'),

    path('delete-bookclub/<str:pk>/', views.deleteBookClub, name='delete-BookClub'),

    path('update-bookclub/<str:pk>/', views.updateBookClub, name='update-BookClub'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('register/', views.registerPage, name='register'),

    path('about',views.about,name='about'),

]