from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Book)
admin.site.register(BookClub)
admin.site.register(Comment)
admin.site.register(Chat_BC)

