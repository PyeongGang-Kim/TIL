from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Article, Comment
from IPython import embed

def index(request):
    articles = Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)
# Create your views here.

# def new(request):
#     embed()
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image=image)
        article.full_clean()
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/create.html')

    # try:
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     article = Article(title=title, content=content)
    #     article.full_clean()
    # except ValidationError:
    #     raise ValidationError('Your Error Message')
    # else:
    #     article.save()
    #     return redirect('articles:detail', article.pk)



    # 1번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # # 2번째 방법
    # article = Article(title=title, content=content)
    # article.save()

    # # 3번째 방법
    # Article.objects.create(title=title, content=content)
    
    # return redirect('/articles/'+str(article.pk))
    #return redirect('article/')로 입력하면 create 뒤에 추가로 article이 붙은상태
    #그걸 막기 위해서 /를 앞에 붙인다.

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    else:
        context = {'article': article}
        return render(request, 'articles/detail.html', context)

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article': article}
#     return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        context = {'article': article}
        return render(request, 'articles/edit.html', context)
    else:
        # embed()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        tmp = request.FILES.get('image')
        if tmp:
            article.image = tmp
        article.save()
        return redirect('articles:detail', article.pk)


def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    res = request.POST.get('content')
    if request.method == 'POST':
        comment = Comment()
        comment.content = res
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)


    else:
        return redirect('articles:detail', article.pk)

        
def comment_delete(request, article_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)


def comment_update(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('articles:detail', article_pk)
    else:
        context = {
            'comment': comment,
        }
        return render(request, 'articles/comment_update.html', context)
