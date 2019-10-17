from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        article = ArticleForm(request.POST).save()

        return redirect('articles:detail', article.pk)
    else:
        
        article_form = ArticleForm()
        context = {
            'article_form': article_form,
        }
        return render(request, 'articles/form.html', context)
    

def detail(request, article_pk):
    comment_form = CommentForm()
    context ={
        'article' : get_object_or_404(Article, pk = article_pk),
        'comment_form': comment_form,
    }

    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    article.delete()
    return redirect('articles:index')


def update(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)

    if request.method =='GET':
        article_form = ArticleForm(instance=article)
        context  = {
            'article': article,
            'article_form': article_form,
        }
        # embed()
        return render(request, 'articles/form.html', context)
    
    else:
        article=ArticleForm(request.POST, instance=article)
        article.save()
        return redirect('articles:detail', article.pk)

@require_POST  
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, id=comment_pk)
    comment.delete()

    return redirect('articles:detail', article_pk)

@require_POST 
def comment_create(request, article_pk):

    comment = CommentForm(request.POST).save(commit=False)
    comment.article_id = article_pk
    comment.save()
    return redirect('articles:detail', article_pk)