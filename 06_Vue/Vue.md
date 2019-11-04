# Vue

MVVM

M model

V DOM

VM View Model(Vue)





익스텐션

Vetur, Vue VSCode Snippets 



cdn활용

vue js 시작하기 검색

상용버전이 아닌 개발 버전으로 가져온다.

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

html 바디 안에 붙여넣어준다.

그럼 그 바로 밑에 script 태그를 열어서 Vue 코드를 작성될 곳을 만든다.



크롬 확장 vue devtools

세부 설정에서 파일 URL에 대한 액세스 허용 활성화



뷰 감지 해줌

f12누르면 console처럼 Vue탭이 생긴다.



뷰의 for

li 속성 중에 v-for="명령어(todo in todos)" 이런식으로 작성한다.

```html
<li v-for="todo in todos">
```

if와 else를 같이 사용할 수 있다.

```html
	// true 인 것 보여주기
<li v-for="todo in todos" v-if="todo.completed">
    // true 아닌 것 보여주기
<li v-for="todo in todos" v-if="!todo.completed">
  {{ todo.content }} {{ todo.completed }}
</li>
<li v-else>[완료!]</li>
```

li태그에  v-on:click="todo.completed = true"추가하면 클릭할 때 값을 바꿔줄 수 있다.





```html

    <img v-bind:src="vueImage">

뷰 data에 
vueImage: 'http://webpds.saramin.co.kr/pds/united_company/logo/9310_logo_2.gif'
```

v-on: 은 @으로 대체가능

v-bind는 생략 가능

함수 안에 함수는 화살표함수를 써야 함.

그게 아닌 메서드에서 바로 쓰는 함수는  function() { }이런식으로 사용해야함.

