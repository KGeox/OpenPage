from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('post/<str:pk>/',views.post,name='post'),
    path('book/<str:pk>/',views.book,name='book'),
    path('bookclub/<str:pk>/',views.bookclub,name='bookclub'),
    path('about',views.about,name='about'),

]