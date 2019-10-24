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

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'form': form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

def delete(request, article_id):
    if request.method=='POST':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
    return redirect('articles:index')


def update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_id)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

def comment_create(request, article_id):
    if request.method=="POST":
        comment = CommentForm(request.POST).save(commit=False)
        comment.article_id = article_id
        comment.save()
    return redirect('articles:detail', article_id)

def comment_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('articles:detail', article_id)