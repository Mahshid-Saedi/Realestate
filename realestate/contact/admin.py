from django.contrib import admin
from .models import PostModel,CommentModel

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'subject', 'update')
    search_fields = ('slug', 'body')
    list_filter = ('update',)
    prepopulated_fields = {'slug':('body',)}
    raw_id_fields = ('user',)

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post', 'created', 'is_reply')
    raw_id_fields = ('user', 'post', 'reply')