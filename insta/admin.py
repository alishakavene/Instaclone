from django.contrib import admin
from .models import User,Post,tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    
admin.site.register(User)
admin.site.register(Post)
admin.site.register(tags)