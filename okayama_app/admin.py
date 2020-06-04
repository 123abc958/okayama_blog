from django.contrib import admin

# Register your models here.

from .models import Post, Tag
 
admin.site.register(Tag)
admin.site.register(Post)
