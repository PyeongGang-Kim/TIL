from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.order_by('-id')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()
    # Article.objects.create(title=title, content=content)
    return redirect('/articles/'+str(article.id)+'/')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('/articles/')