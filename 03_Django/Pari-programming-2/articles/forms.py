from django.forms import ModelForm
from articles.models import Article, Comment

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content',]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
    
