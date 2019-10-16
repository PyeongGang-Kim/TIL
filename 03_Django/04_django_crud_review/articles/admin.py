from django.contrib import admin
from .models import Article, Comment
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    #보여줄 항목 설정
    list_display = ('id', 'title', 'content', 'image', 'created_at', 'updated_at')

    #링크(데이터 튜플을 자세히 보기)
    list_display_links = ['content']

    #필터를 걸 항목
    list_filter = ('created_at', )

    #수정 가능하게 만들 항목
    list_editable = ('title', )

    #한 페이지당 보여줄 게시글 수 설정
    list_per_page = 2
admin.site.register(Article, ArticleAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at',)
    list_filter = ('created_at',)
    list_editable = ('content',)

admin.site.register(Comment, CommentAdmin)