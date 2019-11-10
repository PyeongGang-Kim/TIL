# Java Script

## 기본 세팅

nodejs를 검색해서 다운로드 후 설치

vscode 터미널에서 node 타이핑햇을때 들어가지면 설치 제대로 됨

extension에 Live Server, Auto Close Tag, Rainbow Brackets, indent-rainbow, Beautify



에디터 탭 사이즈를 4에서 2로 바꾼다.

f1누르고 preference쳐서 settings.json에 들어가 파이썬부분을 추가한다.

```json
{
    "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
    "editor.mouseWheelZoom": true,
    "workbench.startupEditor": "newUntitledFile",
    "workbench.iconTheme": "vscode-icons",
    "[python]": {
        "editor.tabSize": 4
    },
    "editor.tabSize": 2
}
```

File Preference Setings에서 Editor: tab Size = 2





var는 ex6이전에 나왔던 선언방법이다. 권장하지 않음

let은 선언 딱 한번만가능. 할당은 자유롭게 할 수 있다.

const는 할당과 선언 딱 한번만 가능. 할당이 되고 난 후에 재할당은 불가능하다.



브라우저 콘솔에서

const userName = prompt('Hello! Who are you?') 를 입력하면

입력 창이 하나가 뜬다

거기에 입력한 값이 userName에 저장이 된다.



```js
const userName = prompt('Hello! Who are you?')
undefined
userName
"ssw"
let message = ''
undefined
switch(userName){
    case '1q2w3e4r': {
        message = '<h1>This is secret admin page.</h1>'
    }
    case 'ssafy':{
        message = '<h1>You are from matrix.</h1>'
    }
    default:{
        message = `<h1>Hello ${userName}.</h1>`
    }
}
"<h1>Hello ssw.</h1>"
document.write(message)
undefined
```



```js
switch(userName){
    case '1q2w3e4r': {
        message = '<h1>This is secret admin page.</h1>'
		console.log(message)
		break
    }
    case 'ssafy':{
        message = '<h1>You are from matrix.</h1>'
		console.log(message)
		break
    }
    default:{
        message = `<h1>Hello ${userName}.</h1>`
		console.log(message)
    }
}
```







## axios

콘솔창에서 npm install axios로 엑시오스 설치하기



랜덤 json파일 받기(100개)

jsonplaceholder.typicode.com

 https://jsonplaceholder.typicode.com/posts 

```js
const axios = require('axios')
axios
.get('https://jsonplaceholder.typicode.com/posts').then(response => {
  console.log(response)
})
.catch(err => {
  console.log(err)
})
```



dog.ceo 사이트에 개 사진 api



lower camel case 첫번째만 소문자 나머지 단어는 대문자로 시작

파스칼 케이스 == upper cammel case

스네이크 케이스 언더바 사용



null 과 undefined는 같은 것이다.

typeof null -> object

typeof undefined -> undefined



nan이 나오는 경우를 알기

'asdf'*3



문자를 표현하는 방법 세가지 싱글 더블 빽틱

==과 ===의 차이는 자동으로 형변환 해서 비교를 해 주는것이다.

1과 == '1'일 때는 true

1과 ==='1' 일 때는 false





에로우 펑션 괄호 지울 수 있는 경우

기본값 주면 괄호 꼭 필요함

안주면 

뒤의 값 생략하는 방법또한 있다.



인자가 하나도 없을 경우 () => 

혹은 _ =>

이렇게 생략할 수 있다.



익명함수 인자 없이 쓰려면 즉시실행

오브젝트에서 키로 밸류 뽑을 때

오브젝트.키

오브젝트["키"]

두글자 이상일 때에는 대괄호를 사용해야만 한다.



어레이 헬퍼

foreach

filter

some, every

reduce

map



setTime 일정 시간 후 실행하기

콜백을 주로 사용함

비동기방식(none blocking) 독립적으로 



1급 객체가 되는 조건

다른 함수에 인자로 넘길 수 있는가

변수에 담을 수 있는가

리턴값이 될 수 있는가

이 세가지를 만족해야 함



돔 조작

이벤트리스너



함수를 호출한 곳이 전역일 경우 this는 전역을 가르킨다

함수를 호출한 곳이 변수 안일 경우 this는 변수를 가르킨다.



에로우함수에서 this는 호출한 곳의 상위의 this를 가르킨다.

변수 안에서 호출하면 변수의 상위(윈도우)를 가르킨다.







헬퍼 메서드

동등 비교 일치 비교 == ===        type of 많이 찍어보기

this 많이 보기

자바스크립트 일꾼 몇명의 일꾼이 있는지

자바 스크립트는 단 하나의 호출 스택(콜 스택)을 사용한다. 이러한 방식을 run to completion이라고 한다.

하나의 함수가 실행되면 함수의 실행이 끝날 때까지 다른 작업이 수행될 수 없다.

비동기로 호출되는 함수들은 call stack이 아닌 task queue(콜백 큐)에 쌓인다



이벤트 루프 돌아가는 것

set time out 비동기 처리. 콜백, 큐스택, 

크리에이트 엘레먼트 쿼리 셀렉터 등 돔 조작 관련

promise를 어떻게 처리 하는지 .then과 .catch 차이

좋아요 엑시오스 구성



