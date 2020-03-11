# REST 서버에 요청을 보내고 받아오기

## 필요한 모듈

json요청을 보내고 받기 위해선 requests와 json모듈이 필요하다

```python
import requests, json
```



## 데이터 전송과 응답의 예

보내는 데이터는

```python
data = {
    "nickname": "구미1반김평강",
    "yourAnswer":"1"
    }

header = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
res = requests.post(url, data=json.dumps(data), headers=header)
```

이와 같은 형식으로 보낸다.

응답은 정답일 경우

```python
{
    'code': 200,
    'nextUrl': 'bravo',
    'question': 'Q2: 지난 SSAFY 3기 입학식에는 크리에이터 펭수가 함께 했습니다. 펭수와의 면접과 입학식 장면이 담긴 유튜브는 에피소드 몇 화였을까요? (정답 OO)'
} 
```

닉네임이 없을 경우

```python
{
    'code':403
}
```

오답일 경우

```python
{
    'code': 600
} 
```

의 형태로 받아온다.



각 퀴즈의 주소는 urlbase+res.jo['nextUrl']의 형태이다.



## 산출물

결과는 다음과 같다.

```bash
1

{
    'code': 200,
    'nextUrl': 'bravo',
    'question': 'Q2: 지난 SSAFY 3기 입학식에는 크리에이터 펭수가 함께 했습니다. 펭수와의 면접과 입학식 장면이 담긴 유튜브는 에피소드 몇 화였을까요? (정답 OO)'
} 

86

{
    'code': 200,
    'nextUrl': 'chopper',
    'question': 'Q3: SSAFY의 인스타그램에는 SSAFY의 여러 모습들이 올라와 있는데요. SSAFY의 소식을 전해주는 기자단의 영문 명칭은 무엇일까요?'
}

ssafycial

{
    'code': 200,
    'nextUrl': 'weekend',
    'question': 'Q4: 교차 출처 리소스 공유(Cross Origin Resource Sharing)는 추가적인 http 헤더를 이용하여, 한 출처에서 실행 중인 웹 애플리케이션이 다른 출처의\n자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 것을 말합니다. 자원의 출처가 다르다 는 것은 3가지 요소를 가지고 파악하는데요.\n3가지 요소에는 domain, port, 그리고 이것이 있습니다. 이것은 무엇일까요? (영문)'
}

protocol

{
    'code': 200,
    'nextUrl': 'river',
    'question': 'Q5: 이것은 경량의 데이터 교환 형식으로, 사람과 기계가 읽고 쓰기에 용이하며, Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의\n데이터 포맷이다. 객체를 나타낼 때 중괄호로 시작해서 중괄호로 끝나는 이것은 무엇인가? (영문, 약자)'
}

json

{
    'code': 200,
    'nextUrl': 'hand',
    'question': 'Q6: 이것은 프로그램 내에서 인스턴스가 오직 하나만 생성되는 것을 보장하고, 프로그램 어디서든 이 인스턴스로의 접근을 허용하는 것입니다. 이 패턴은 무엇일까요?\n(영문, OOOO pattern)'
}

singleton

{
    'code': 200,
    'nextUrl': 'over',
    'question': 'Q7: 브라우저에 데이터를 저장하는 방법에는 storage, indexed DB, 그리고 이것이 있습니다. session ID를 저장하는 용도로도 사용되는 이것은 무엇일까요? 
(영문)'
}

cookie

{
    'code': 200,
    'nextUrl': 'hello',
    'question': 'Q8: 이것은 Remote Dictionary Server의 약자로, 키-값 구조의 비정형 데이터를 저장하고 관리하기 위한 오픈 소스 비관계형 DBMS다.\n인스타그램, LINE 등에서 널리 사용되는 이것은? (영문)'
}

redis

{
    'code': 200,
    'nextUrl': 'python',
    'question': 'Q9: 이것은 디자인 패턴의 하나로 Model + View + View Model을 합친 말이다. View와 Model 사이에 의존성을 없애고 모듈화를 가능하게 만든 이것은?(영문, OOOO pattern)'
}

mvvm

{
    'code': 200,
    'nextUrl': 'java',
    'question': 'Q10: 이것은 파이썬의 라이브러리로 데이터 조작 및 분석을 위해서 주로 사용된다. pd라는 약어로 주로 사용되는 이것은? (영문)'
}
    
pandas

{
    'code': 200,
    'nextUrl': 'script',
    'question': 'Q11: 이것은 근거리 무선 통신 기술의 하나로 2.4Ghz 대역폭을 사용한다. 갤럭시 버즈와 같은 무선 이어폰에 주로 사용되며, 덴마크의 왕인 하랄 블로탄의 이름에서 유래한 이것은? (영문)'
}

bluetooth

{
    'code': 200,
    'nextUrl': 'zero',
    'question': 'Q12: SSAFY 1기 교육생들이 출시한 앱으로, 삼성전자 해외연구소 파견 교육과정 중 우크라이나 팀에서 개발한 헬스케어 앱의 이름은? (영문)'
}

fittymon

{
    'code': 200,
    'nextUrl': 'coat',
    'question': 'Q13: In computing, this is an optimization technique used primarily to speed up computer programs by storing results of expensive\nfunction calls and returning the cached result when the same inputs occur again. What is this? (영문)'
} 

memoization

{
    'code': 200,
    'nextUrl': 'sand',
    'question': 'Q14: 전통적인 프로그래밍에서는 개발자가 작성한 프로그램이 외부 라이브러리 코드를 호출한다. 그러나 이것이 적용된 구조에서는 외부 라이브러리 코드가 개발자가 작성한 코드를 호출한다.\n이것은 무엇인가? (영문, 약자로 쓰시오)'
}

ioc

{
    'code': 200,
    'nextUrl': 'king',
    'question': 'Q15: 이것은 리눅스의 응용 프로그램들을 소프트웨어 컨테이너 안에 배치시키는 일을 자동화하는 오픈 소스이다. 리눅스에서 운영체제 수준 가상화의 추상화 및 자동화 계층을 추가적으로\n제공하기도 하는 이것은 무엇인가? (영문)'
}

docker

{
    'code': 200,
    'nextUrl': 'knight',
    'question': 'Q16: 루트 노드에서 시작해서 다음 분기로 넘어가기전에 해당 분기를 완벽하게 탐색하는 방법으로, 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수\n없게 되면 다시 가장 가까운 갈림길로 돌아와서 다른 방향으로 다시 탐색을 진행하는 것과 유사한 이것은? (영문 3글자, 약자로 쓰시오)'
}

dfs

{
    'code': 200,
    'nextUrl': 'great',
    'question': 'Q17: 삼성 갤럭시 Z 플립은 안드로이드 스마트폰으로 폴더블 디스플레이를 탑재했다. 갤럭시 Z 플립의 개발 코드 네임은? (영문)'
}

bloom

{
    'code': 200,
    'nextUrl': 'again',
    'question': 'Q18: SSAFY의 공식 영문 명칭에서 가장 많이 등장하는 알파벳은? (영문)'
}

a

{
    'code': 200,
    'nextUrl': 'ring',
    'question': 'Q19: 이 정렬 방법은 토니 호어가 고안한 방법으로, 다른 원소와의 비교만으로 정렬을 수행하는 비교 정렬 방법의 하나이다. 평균적으로 O(n log n)의 시간복잡도를 가지는\n이 정렬은 무엇인가? (영문, OOO sort)'
}

quick

{
    'code': 200,
    'nextUrl': 'jordan',
    'question': 'Q20: 이것은 컨테이너화된 애플리케이션의 자동 배포, 스케일링 등을 제공하는 관리시스템으로 오픈 소스이다. 구글에 의해 설계되었고, 리눅스 재단에 의해 관리되고 있으며\n도커와 같은 컨테이너 도구와 함께 동작하는 이것은 무엇인가? (영문)'
}

kuvernetes

{
    'code': 600,
    'nextUrl': '',
    'question': ''
}

kubernetes

{
    'nextUrl': '수고하셨습니다.',
    'code': 200,
    'question': '모든 문제를 완료하셨습니다.'
}
```

