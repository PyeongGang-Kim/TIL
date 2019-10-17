from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.views.decorators.http import require_POST
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
    '''
    Form class
    모델에 대한 정보를 알지 못해서 유효성 검사 이후에
    cleaned_data를 통해 데이터 정제 후 DB에 실제 저장하는 로직이 필요함.

    Model Form
    이미 Model에 대한 정보(스키마)를 알고 있기 때문에 어떤 모델에 레코드를 넣어야 하는지
    알고 있고 form.save()만 해도 DB에 저장이 됨.
    '''
    if request.method == "POST":
        # 폼 인스턴스 생성하고 요청에 의한 데이터로 채운다.
        form = ArticleForm(request.POST)
        # 해당 폼이 유효한지 확인
        if form.is_valid():
            # # form.cleaned_data를 통해 폼 데이터를 정제한다.
            # # form.cleaned_data는 딕셔너리 형태로 유효한 값들만 보낸다.
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)

            # 폼에 article을 로드하고 meta에 불러왔기 때문에 가능한 방법
            # form.save()를 하면 article 객체를 반환해 준다.
            article = form.save()
            # embed()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        # embed()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comments.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # article.title = form.cleaned_data.get('content')
            # form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    # embed()
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/form.html', context)

@require_POST
def comments_create(request, article_pk):
    comment_form = CommentForm(request.POST)
    
    # embed()
    if comment_form.is_valid():
        # commit=False는 바로 저장하진 않는다는 말임 (기본값 True)
        # comment에 id가 없기때문에 저장되지 않으므로 articleid를 추가해 줄 수 있다.
        # 그 후 저장.
        comment = comment_form.save(commit=False)
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)


def comments_update(request, article_pk, comment_pk):
    # if request.method == 'POST':
        
    #     article = get_object_or_404(Article, pk=article_pk)
    #     comment_form = CommentForm(initial = {
    #         'content'=content,
    #     })

    #     comments = article.comments.all()
    #     context = {
    #         'article': article,
    #         'comment_form': comment_form,
    #         'comments': comments,
    #     }
    #     return render(request, 'articles/detail.html', context)




    #     comment = get_object_or_404(Comment, pk=comment_pk)
    #     context = {
    #         'comment': comment)
    #     }
    pass

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)


'''
create 로직
1. get
사용자가 데이터를 입력할 수 있는 form을 제공
2. post
사용자가 보낸 새로운 글을 db에 저장

update 로직
1. get
기존 사용자의 글이 입력된 form 제공
2. post
수정된 글을 db에 저장
'''