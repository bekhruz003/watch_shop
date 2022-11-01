from django.contrib import admin
from .models import *


@admin.register(PostTagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['title']
    list_filter = ['created_at']
    search_fields = ['title', 'body']
    autocomplete_fields = ['auther', 'tag', 'category']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'site']
    list_display_links = ['name', 'email', 'site']
    list_filter = ['created_at']


@admin.register(AutherModel)
class AutherModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']
    search_fields = ['full_name']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
