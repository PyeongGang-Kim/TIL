from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment, Hashtag
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ArticleForm, CommentForm
from IPython import embed
import hashlib
# Create your views here.

def index(request):
    # 1. 세션 정보에서 visits_num 이라는 키로 접근해 값을 가져옴
    # 해당하는 키가 없으면 0 을 가져옴
    visits_num = request.session.get('visits_num', 0)

    # 2. 가져온 값을 session에 'visits_num'이라는 새로운 키의 값으로 1씩 증가
    request.session['visits_num'] = visits_num+1

    # 3. 세션 데이타를 수정하면 장고는 수정한 내용을 알 수 없어서 작성하는 코드
    request.session.modified = True
    # embed()



    articles = Article.objects.all()
    context = {
        'visits_num': visits_num,
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required()
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
            article = form.save(commit=False)
            article.user_id = request.user.id
            article.save()
            # embed()
            # 1. content를 공백 기준으로 리스트로 변경 후 for문
            for word in article.content.split():
                # 2. '#'으로 시작하는 요소를 선택
                if word.startswith('#'):
                    # 3. word랑 같은 해시 태그를 찾고 있으면 기존 객체를, 없으면 새로운 객체 생성
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    # 4. 게시글의 해시태그 목록에 해당 단어를 추가
                    article.hashtags.add(hashtag)

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
    person = get_object_or_404(get_user_model(), pk=article.user.pk)
    comments = article.comments.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
        'person': person,
    }
    # embed()
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:
            article.delete()
    return redirect('articles:index')

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                # article.title = form.cleaned_data.get('content')
                article = form.save()
                article.hashtags.clear()
                for word in article.content.split():
                    if word.startswith('#'):
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        article.hashtags.add(hashtag)
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        # embed()
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/form.html', context)

@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        
        # embed()
        if comment_form.is_valid():
            # commit=False는 바로 저장하진 않는다는 말임 (기본값 True)
            # comment에 id가 없기때문에 저장되지 않으므로 articleid를 추가해 줄 수 있다.
            # 그 후 저장.
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.user_id = request.user.id
            comment.save()
    return redirect('articles:detail', article_pk)

@login_required()
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
    #         'comment': comment,
    #     }
    pass

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
    return redirect('articles:detail', article_pk)


@login_required
def like(request, article_pk):
    if request.is_ajax():
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user

        # 해당 게시글에 좋아요를 누른 사람들 중에서
        # user.pk(현재 요청 유저)를 가진 user가 존재하면
        # 좋아요 취소
        #아니면 좋아요 목록에 유저 추가
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            liked = False
        else:
            article.like_users.add(user)
            liked = True
        context = {
            'liked': liked,
            'count': article.like_users.count(),
        }
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()

@login_required
def follow(request, article_pk, user_pk):
    # 게시글을 작성한 유저
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # 해당 경로로 요청을 보낸 사람
    user = request.user

    # 해당 person의 팔로워 중에서 요청을 보낸 사람이 존재 하면 언팔로우
    if person.followers.filter(pk=user.pk):
        person.followers.remove(user)
    # 존재하지 않으면 팔로우
    else:
        person.followers.add(user)
    return redirect('articles:detail', article_pk)


@login_required
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')
    context = {
        'hashtag': hashtag,
        'articles': articles,
    }
    return render(request, 'articles/hashtag.html', context)


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
