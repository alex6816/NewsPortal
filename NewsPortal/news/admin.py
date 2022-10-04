from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'categoryType', 'dateCreation')
    list_filter = ('title', 'author', 'dateCreation')
    search_fields = ('title', 'dateCreation')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


# Register your models here.
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(CategorySubscribers)
