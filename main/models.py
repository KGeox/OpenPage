from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.jpg', upload_to='Images/profile_pics')
    bio = models.TextField()
    streak = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    image = models.ImageField(default='default.jpg', upload_to='Images/posts')
    reads = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " by " + self.author.user.username

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('romance', 'Romance'),
        ('non-fiction', 'Non-fiction'),
        ('fantasy', 'Fantasy'),
        ('sci-fi', 'Sci-Fi'),
        ('historical', 'Historical'),
        ('mystery', 'Mystery'),
        ('biography', 'Biography'),
        ('philosophy', 'Philosophy'),
        ('poetry', 'Poetry'),
        ('horror', 'Horror'),
        ('adventure', 'Adventure'),
        ('psychology', 'Psychology'),
        ('other', 'Other'),
    ]
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    image = models.ImageField(default='default.jpg', upload_to='Images/books')
    genre = models.TextField(max_length= 100, choices=GENRE_CHOICES, default="other")
    summary = models.TextField(max_length=5000, null=True)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " by " + self.author

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.author.user.username + " wrote " + "'" + self.content +"'"

class BookClub(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    host = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='host')
    members = models.ManyToManyField(Profile, blank=True, related_name='members')
    current_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " hosted by " + self.host.user.username

class Chat_BC(models.Model):
    bookClub = models.ForeignKey(BookClub, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    date_updated = models.DateTimeField(auto_now=True)
    date_written = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user.username + " wrote " + "'" + self.content +"'"