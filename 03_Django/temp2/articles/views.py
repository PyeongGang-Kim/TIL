from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed

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
    article = Article.objects.get(id=article_id)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == "GET":
        article_form = ArticleForm(article)
        context = {
            'article_form': article_form,
        }
        print(dir(article_form))
        return render(request, 'articles/form.html', context)
    else:
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article_id)

def delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return redirect('articles:index')

def comment_create(request, article_id):
    if request.method == 'POST':
        comment = CommentForm(request.POST).save(commit=False)
        comment.article_id = article_id
        comment.save()
        return redirect('articles:detail', article_id)

def comment_delete(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        article_id = comment.article_id
        comment.delete()
        return redirect('articles:detail', article_id)
