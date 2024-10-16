from django.contrib import admin
from .models import Game, Comment, Like


# Register your models here.

admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(Like)