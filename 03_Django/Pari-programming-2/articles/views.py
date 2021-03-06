from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST
from IPython import embed

def index(request):
    articles = Article.objects.all()
    # embed()
    context = {'articles':articles,}
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context= {'form': form,}
    return render(request, 'articles/forms.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk= article_pk)
    # embed()
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context ={'article':article, 'comments':comments, 'comment_form':comment_form, }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk= article_pk)
    article.delete()
    return redirect('articles:index')

def update(request, article_pk):
    article = get_object_or_404(Article, pk= article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance= article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
    else:
        form = ArticleForm(instance= article)
    context= {'form': form,}
    return render(request, 'articles/forms.html', context)

@require_POST
def comment_create(request, article_pk):
    comment = CommentForm(request.POST).save(commit=False)
    comment.article_id = article_pk
    comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

def likearticle(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # embed()

    if article.like_users.filter(pk=request.user.id):
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
        
    
    return redirect('articles:detail', article_pk)