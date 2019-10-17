from django.contrib import admin
from .models import Article, Comment

# Register your models here.

# 1번 방법
@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

# 2번 방법
# admin.site.register(Article, ArticleAdmin)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at',)

# admin.site.register(Comment, CommentAdmin)