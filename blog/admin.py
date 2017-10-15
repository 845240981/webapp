from django.contrib import admin
from .models import Post,Comment
# Register your models here.

class Postadmin(admin.ModelAdmin):
    list_display = ('title','author','publish','status')
    list_filter = ('status', 'created', 'publish', 'author')

admin.site.register(Post,Postadmin)

class Commetadmin(admin.ModelAdmin):
    list_display = ('post','name','body','active')
    list_filter = ('created',)

admin.site.register(Comment,Commetadmin)