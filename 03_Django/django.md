# django

## 가상환경 실행하기

```bash
student@DESKTOP MINGW64 ~/TIL/03_Django/01_django_intro (master)
$ python -m venv venv

student@DESKTOP MINGW64 ~/TIL/03_Django/01_django_intro (master)
$ source venv/Scripts/activate
(venv)
student@DESKTOP MINGW64 ~/TIL/03_Django/01_django_intro (master)
$
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
```

이런식으로 만들고 나서

python manage.py makemigrations 명령어를 사용한다.

그렇게하면 migrations폴더에 파이썬 파일이 만들어진다.(확인용)

python manage.py migrate 입력하면 db에 작성됨

sqlite 익스텐션 설치 해 준 후 f1눌러서 sqlite검색 하여 open database로 데이터베이스 열어준다.

익스플로러 맨 밑에 나온다.



## 장고 쉘

python manage.py shell 명령하면 파이썬 + 장고 쉘 실행된다.

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

