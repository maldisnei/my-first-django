from django.contrib import admin

from . models import Post,Comment
from .models import Sobre_mim

admin.site.register(Sobre_mim)
admin.site.register(Post)
admin.site.register(Comment)

