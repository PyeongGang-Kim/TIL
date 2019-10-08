# django

## 가상환경 실행하기

```bash
student@DESKTOP MINGW64 ~/TIL/03_Django/01_django_intro (master)
$ python -m venv venv

student@DESKTOP MINGW64 ~/TIL/03_Django/01_django_intro (master)
$ source venv/Scripts/activate
(venv)
```

## 가상환경 종료하기

```bash
$deactivate
```

## 코드에서 자동으로 가상환경 들어가게 만들기

vs코드에서 f1누르고 select interpreter 입력

## 장고 프로젝트 만들기

```bash
$ django-admin startproject django_intro .
							 (프로젝트 명)
```

## 장고 서버 실행

```bash
$ python manage.py runserver
```

## 장고 앱 실행

```bash
$ python manage.py startapp pages
							(앱 명)
```

앱이 만들어진다.

앱이 만들어지고 난 후 장고 프로젝트의 settings에 INSTALLED_APPS리스트에 앱 명을 추가해 준다.

## 세팅

초기 앱 만들고 나서 urls.py에서 from 앱이름 import views로 views를 추가해준다.



## 스태틱 이미지 주소 넣어주기

html 파일 맨 위에 {% load static %}를 입력해준다.

tmplates 폴더와 같은 경로에 있는 static 폴더에 접근하게 된다.

정적인것들(스타일, 이미지 등은 static을 먼저 접근한다.)



## URL을 앱별로 관리하기

urls.py 파일에서

```python
from django.urls import path, include
```

include를 추가해준다.

urlpatterns리스트에     path('pages/', include('pages.urls')), 추가해준다.

​													앱이름

그 후 app폴더 안에 urls.py를 만들어 주고

```python
from django.urls import path
from . import views
#현재 디렉토리인경우 . 써줌
	

urlpatterns = [
    
]
```

입력한다.



pages/index를 들어가도 utilities의 index를 열어버리는 문제가 발생함.

installed apps를 위에서부터 조회하면서 내려가기 때문임

이를 방지하기 위해 templates폴더 안에 앱이름 폴더를 다시 만들고 html문서들을 거기에 넣어준다.

그 후 view파일에 html경로를 html이름에서 앱이름/html이름으로 변경해준다



## 템플릿 상속

네브바 같이 모든 페이지에서 계속 사용할 것들은 베이스에 등록 한 후 상속하면 된다.

프로젝트 폴더 안에 templates폴더 생성 후 base.html을 만들어 준다.

앱 내부에 없기때문에 찾지 못한다. 따라서 settings.py의 TEMPLATES 리스트를 본다.

DIRS리스트에 os.path.join(BASE_DIR, 'django_intro', 'templates')를 추가해 준다.

내부 옵션 중 APP_DIRS가 True로 되있기 때문에 앱 내부의 템플릿을 찾아가는 것임.

모두 세팅 한 후 물려받고 싶은 html파일의 맨 위에 {% extends 'base.html' %}를 입력해 준다.

그 다음 바디 내용을

원래 

```html
{{ area }}
```

에서 

```html
<!-- base.html파일을 전부 불러온다. -->
{% extends 'base.html' %}

<!-- base.html 안의 블록 안에 원하는 내용을 추가할 수 있다. -->
{% block body %}
{{ area }}
{% endblock %}
```

로 바꿔준다.



폼 액션의 GET와 POST 차이

폼에서 보낼때 POST의 경우    {% csrf_token %}를 추가해줘야 함

views.py 파일에서 받을때 폼 안에  

​    word = request.POST.get('word')

​    word = request.GET.get('word')





## 데이터베이스

models.py 에서

```python
class Article(models.Model):
    # CharField는 글자수 제한이 필수
    title = models.CharField(max_length=10)
    # TextField는 글자수 제한 필요없음
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'제목: {self.title}, 내용: {self.content}'
```

이런식으로 만들고 나서

python manage.py makemigrations 명령어를 사용한다.

그렇게하면 migrations폴더에 파이썬 파일이 만들어진다.(확인용)

python manage.py migrate 입력하면 db에 작성됨

sqlite 익스텐션 설치 해 준 후 f1눌러서 sqlite검색 하여 open database로 데이터베이스 열어준다.

익스플로러 맨 밑에 나온다.

python manage.py sqlmigrate app이름 0001 명령을 하면 데이터베이스 정의를 볼 수 있다.

python manage.py showmigrations를 하면 볼 수 있다.



## 장고 쉘

python manage.py shell 명령하면 파이썬 + 장고 쉘 실행된다.

(python manage.py shell_plus는 장고 익스텐션 설치 후 가능

import 자동으로 해 준다.)

from articles.models import Article 명령을 통해 원하는 데이터베이스 클래스(articles 앱의 models.py에서Article 테이블)를 불러온다

Article 테이블의 모든 객체 불러오기: Article.objects.all()

Article.objects.all()

1번째 방법

>>> article = Article()
>>> article.title = 'first'
>>> article.content = 'django!'
>>>
>>> article.save()



2번째 방법

article = Article(title='second', content='django!')

article.save()



3번째 방법(바로 저장됨)

Article.objects.create(title='third', content='django!')



### 유효성 검사

저장하기 전 인스턴스에 .full_clean() 메서드를 이용하면 검사를 해준다.

models에서 정의한 클래스를  def __str__(self):를 보기 쉽게 편집할 수 있다.

```python
def __str__(self):
    return f'{self.id}번글 - {self.title}: {self.content}'
```

articles = Article.objects.all()을 통해 모든 데이터베이스를 articles변수에 담을 수 있다.



### 필터 사용법

```bash
>>> articles = Article.objects.filter(title='first')
>>> articles
<QuerySet [1번글 - first: django!, 4번글 - first: haha]>

필터에서 .first()를 통해 한번 더 필터링 할 수 있다. .last() 사용가능 첫번째, 마지막꺼만 가져옴
>>> articles = Article.objects.filter(title='first').first()
>>> articles
1번글 - first: django!
```



### 원하는 것 가져오기

```bash
>>> article = Article.objects.get(pk=1)
>>> article
1번글 - first: django!
```

.get의 경우 중복된 데이터가 존재할 경우 오류가 난다.

```bash
>>> article = Article.objects.get(pk=10)
>>> article
오류발생
```

없는 값으로 조회하려고 하는 경우 에러가 난다.



따라서 .get은 pk(기본 키)에서만 사용한다. 그 외에는 filter 사용함.

filter은 없는 값 조회해도 빈 쿼리를 반환하기 때문에 에러가 나지 않는다.



### 정렬

```bash
id 기준으로 오름차순 정렬
>>> articles = Article.objects.order_by('id')
id 기준으로 내림차순 정렬
>>> articles = Article.objects.order_by('-id')
```



### 값 하나 빼오기

```
모든 데이터 가져온 리스트 중 1번 인덱스 하나 가져옴. (객체 한개만 가져옴)
>>> article = Article.objects.all()[1]
```



### 슬라이싱

```bash
인덱스 1, 2번 가져오는 법
>>> article = Article.objects.all()[1:3]
```



### 검색, 필터링

```bash
필터의 경우 갯수 상관 없이 쿼리 셋을 반환한다.

타이틀 내부에 fir이 포함되어 있는 것들만 가져옴
>>> articles = Article.objects.filter(title__contains='fir')
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 4번글 - first: haha>, <Article: 5
번글 - first: vacation>]>

타이틀이 first로 시작하는 것들만 가져옴
>>> articles = Article.objects.filter(title__startswith='first')
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 4번글 - first: haha>, <Article: 5
번글 - first: vacation>]>

content가 !로 끝나는 것들만 가져옴
>>> articles = Article.objects.filter(content__endswith='!')
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 4번글 - first: haha>, <Article: 5
번글 - first: vacation>]>
```



### 업데이트

```bash
첫번째 객체 가지고옴
>>> article = Article.objects.get(pk=1)
타이틀을 변경 후 저장.
>>> article.title='byebye'
>>> article.save()
확인
>>> Article.objects.all()
<QuerySet [<Article: 1번글 - byebye: django!>, <Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>, <Article: 4번글 - first: haha>, <Article: 5번글 - first: vacation>]>
```



### 삭제

```bash
하나의 객체 가지고 옴
>>> article = Article.objects.get(pk=1)
삭제하기
>>> article.delete()
확인
<QuerySet [<Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>, <Article: 4번글 - first: haha>, <Article: 5번글 - first: vacation>]>
```



## 관리자 모드

### 관리자 계정 만들기

```bash
사용자 이름 (leave blank to use 'student'): admin
이메일 주소:
Password:
Password (again):
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
비밀번호가 너무 일상적인 단어입니다.
비밀번호가 전부 숫자로 되어 있습니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

### 관리자 페이지에서 데이터베이스 보기

admin.py 파일에

```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

입력하면 Article 데이터베이스를 관리자페이지(/admin)에서 확인할 수 있다.

### 어드민 페이지 커스텀

```python
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at']
admin.site.register(Article, ArticleAdmin)
```

Article을 list_display에 맞게 보여준다.



## 장고 익스텐션

### 장고 익스텐션 설치

```bash
pip install django-extensions
```

그 후 settings 파일의 INSTALLED_APPS의 맨 밑에 'django_extensions'를 추가해 준다.

이렇게 설정한 후에는

python manage.py shell을 했을때에는 따로 import했던것들(데이터베이스 등)을 하지 않고 바로 사용할 수 있는 python manage.py shell_plus를 사용 가능함.





## CRUD

views.py에서 데이터베이스에 접근하려면

views.py에 데이터베이스 임포트

```python
from .models import Article
```

그 후 장고 쉘에서 했던것처럼 코드 작성해주면 된다.

```python
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()
    
    return render(request, 'articles/create.html')
```



### redirect

views.py에 redirect를 임포트해주고

```python
from django.shortcuts import render, redirect
```

리턴 부분의 리턴 렌더를

```python
    return redirect('/articles/')
```

로 고치면 redirect를 사용할 수 있게 된다.

### 장고 익스텐션

settings 의 installed_apps에 django_extentions 를 추가한다.





### ㅇㄹㅇㄹ

python manage.py sqlmigrate jobs 0001

입력하면 jobs 앱의 0001번 설계도를 확인할 수 있다.

python manage.py showmigrations 현재 데이터베이스 상태 볼 수 있다.



### 해야하는 것

- urls

  - url 분리
  - app_name, path name 설정

- views

  - index: index.html 렌더링
  - past_life: 사용자가 form으로 넘긴 데이터와 faker 라이브러리를 활용해 전생 직업 생성
    - 사용자가 form을 통해 날린 이름을 받는다.
    - DB에 사용자에게 받은 이름이 존재하는지 확인
      - 존재 시 기존 사용자의 past_job을 past_job 이라는 변수에 저장
      - 존재하지 않을 시 faker를 활용하여 새로운 직업을 생성하고 입력받은 사용자의 이름과 새로 생성한 직업을 DB에 저장
    - context로 담아서 past_life.html로 넘김
    - 

- templates

  - 템플릿 구조는 app/templates/app

  - base.html 기존 프로젝트 폴더에서 확장

  - index.html 사용자에게 자신의 이름을 입력할 수 있는 form 제공

  - past_life.html context로 넘겨 받은 데이터를 출력

    ex)  {{ person.name }}님의 전생 직업은 {{ person.past_job }} 입니다.



### 경로를 앱 이름, 경로 이름으로 입력하는 방법

urls.py에서

```python
app_name = 'jobs'

urlpatterns = [
    path('', views.index, name='index'),
    path('past_life', views.past_life, name='past_life'),
]

```

이런식으로 앱 이름과 경로 이름을 지정해 준다.

```html
    <form action="{% url 'jobs:past_life' %}" method="post">
					<!-- 앱이름:경로이름 -->
        {% csrf_token %}
        <label for="name">NAME</label>
        <input type="text" name="name" id="name"><br>
        <input type="submit" value="이름 전송">
    </form>
```

위와 같이 사용할 수 있다.



### 게시글에 덧글 달기

articles의 models.py에 아래와 같이 작성해 준다.

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk', ]
    
    def __str__(self):
        return f'댓글: {self.content}'
```

마이그레이션 후 장고 쉘에서 모델을 확인해 본다.

```bash

In [2]: article=Article.objects.get(pk=18)

In [3]: article
Out[3]: <Article: 제목: dfs, 내용: qg>

In [5]: comment = Comment()
In [6]: comment.content = 'frist comment'
In [8]: comment.article=article
In [9]: comment.save()

In [10]: comment.pk
Out[10]: 1

In [11]: comment.content
Out[11]: 'frist comment'

In [12]: comment.article
Out[12]: <Article: 제목: dfs, 내용: qg>

In [13]: comment.article.id
Out[13]: 18

In [14]: comment.article_id
Out[14]: 18
###############
In [16]: comment = Comment(article=article, content='second comment')
In [17]: comment.save()

In [18]: comment
Out[18]: <Comment: 댓글: second comment>

In [19]: comment.article.title
Out[19]: 'dfs'

In [20]: comment.article
Out[20]: <Article: 제목: dfs, 내용: qg>

In [21]: comment.article.id
Out[21]: 18

#################
In [22]: comment = Comment(article_id=article.pk, content='third comment')
In [23]: comment.save()
```



comment admin페이지 설정

```python

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at',)
    list_filter = ('created_at',)
    list_editable = ('content',)

admin.site.register(Comment, CommentAdmin)
```



```python
In [4]: article = Article.objects.get(pk=18)

In [5]: article.comment_set.all()
Out[5]: <QuerySet [<Comment: 댓글: third comment>, <Comment: 댓글: second comment>, <Comment: 댓글: frist comment>]>

In [6]: dir(article)
Out[6]: 
['DoesNotExist',
 'MultipleObjectsReturned',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_check_column_name_clashes',
 '_check_constraints',
 '_check_field_name_clashes',
 '_check_fields',
 '_check_id_field',
 '_check_index_together',
 '_check_indexes',
 '_check_local_fields',
 '_check_long_column_names',
 '_check_m2m_through_same_relationship',
 '_check_managers',
 '_check_model',
 '_check_model_name_db_lookup_clashes',
 '_check_ordering',
 '_check_property_name_related_field_accessor_clashes',
 '_check_single_primary_key',
 '_check_swappable',
 '_check_unique_together',
 '_do_insert',
 '_do_update',
 '_get_FIELD_display',
 '_get_next_or_previous_by_FIELD',
 '_get_next_or_previous_in_order',
 '_get_pk_val',
 '_get_unique_checks',
 '_meta',
 '_perform_date_checks',
 '_perform_unique_checks',
 '_save_parents',
 '_save_table',
 '_set_pk_val',
 '_state',
 'check',
 'clean',
 'clean_fields',
 'comment_set',
 'content',
 'created_at',
 'date_error_message',
 'delete',
 'from_db',
 'full_clean',
 'get_deferred_fields',
 'get_next_by_created_at',
 'get_next_by_updated_at',
 'get_previous_by_created_at',
 'get_previous_by_updated_at',
 'id',
 'objects',
 'pk',
 'prepare_database_save',
 'refresh_from_db',
 'save',
 'save_base',
 'serializable_value',
 'title',
 'unique_error_message',
 'updated_at',
 'validate_unique']
```



```python
In [20]: comments = article.comment_set.all()

In [21]: comments.first()
Out[21]: <Comment: 댓글: third comment>

In [22]: comments.last()
Out[22]: <Comment: 댓글: frist comment>

#인덱싱으로 접근하는 것도 가능하다.(-1인덱스는 불가능)
In [37]: comments[0].content
Out[37]: 'third comment'

In [23]: for comment in comments.iterator():
    ...:     print(comment)
    ...: 
댓글: third comment
댓글: second comment
댓글: frist comment
    
In [30]: for comment in comments:
    ...:     print(comment)
    ...: 
댓글: third comment
댓글: second comment
댓글: frist comment

```



models에 related name을 설정하면

```python

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk', ]
    
    def __str__(self):
        return f'댓글: {self.content}'
```

article.comment_set.all() 가 불가능해지고

article.comments 로 사용해야 함(comments 는 related_name='comments' 에서 설정한 것)

쿼리셋의 경우 인덱싱, 슬라이싱 가능하다.

