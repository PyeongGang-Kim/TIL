from django.contrib import admin
from .models import Article, Comment
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at', ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', ]

admin.site.register(Comment, CommentAdmin)


admin.site.register(Article, ArticleAdmin)

