from django.contrib import admin
from .models import Editor, Post, tags

admin.site.register(Editor)
admin.site.register(Post)
admin.site.register(tags)
