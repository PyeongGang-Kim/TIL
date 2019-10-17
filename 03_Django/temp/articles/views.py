from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'GET':
        article_form = ArticleForm()
        context = {
            'article_form': article_form,
        }
        return render(request, 'articles/create.html', context)
    else:
        article = ArticleForm(request.POST).save()

        return redirect('articles:detail', article.pk )


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comment_set.all()
    
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
