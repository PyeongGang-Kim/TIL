from django.shortcuts import render, redirect
from .models import Article
from pprint import pprint
from IPython import embed

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('/articles/'+str(article.pk))

def new(request):
    
    return render(request, 'articles/new.html')

def detail(request, pk):
    # pprint(dir(request))
    # print(request.method)
    embed()
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('/articles/'+str(article.pk))

    

