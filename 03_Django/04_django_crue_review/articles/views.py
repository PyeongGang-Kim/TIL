from django.shortcuts import render, redirect
from .models import Article
def index(request):
    articles = Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)
# Create your views here.

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2번째 방법
    # article = Article(title=title, content=content)
    # article.save()

    # 3번째 방법
    Article.objects.create(title=title, content=content)
    
    return redirect('/articles/')
    #return redirect('article/')로 입력하면 create 뒤에 추가로 article이 붙은상태
    #그걸 막기 위해서 /를 앞에 붙인다.

def detail(request, pk):
    pass