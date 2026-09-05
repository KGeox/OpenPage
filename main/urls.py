from allauth.idp.oidc.internal.oauthlib.authorization_codes import lookup
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register("books", views.BookViewSet)

book_router = routers.DefaultRouter(router, "books",lookup='book')
book_router.register("ratings", views.B_ratingViewSet, basename= "rating")

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('profile-edit/', views.editProfile, name='edit-profile' ),
    path('post/<str:pk>/',views.post,name='post'),
    path('book/<str:pk>/',views.book,name='book'),
    path('bookclub/<str:pk>/',views.bookclub,name='bookclub'),
    path('create-book', views.createBook, name='create-Book'),
    path('create-bookclub', views.createBookClub, name='create-BookClub'),
    path('create-post', views.createPost, name='create-Post'),
    path('update-post/<str:pk>/', views.updatePost, name='update-Post'),
    path('delete-post/<str:pk>/', views.deletePost, name='delete-Post'),
    path('like/<int:pk>/', views.toggle_like, name='toggle-like'),
    # path('update-bookclub', views.updateBookClub, name='update-BookClub'),
    path('delete-bookclub/<str:pk>/', views.deleteBookClub, name='delete-BookClub'),
    path('update-bookclub/<str:pk>/', views.updateBookClub, name='update-BookClub'),
    path('delete-comment/<str:pk>/', views.deleteComment, name="delete-comment"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('about',views.about,name='about'),
    path("router", include(router.urls)),
    path("book_router", include(book_router.urls))

]