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

함수 안에 함수는 화살표함수를 써야 함.(그냥 함수를 정의하면 안의 함수는 window를 바라보기 때문. 화살표함수는 바로 위의 함수를 본다.)

그게 아닌 메서드에서 바로 쓰는 함수는  function() { }이런식으로 사용해야함.





```js
        clearCompleted: function(){
          const notCompletedTodos = this.todos.filter((todo) =>{
            return !todo.completed
          })
          this.todos = notCompletedTodos
        }
```





```js
<input type="checkbox" v-model="todo.completed">
```

v-model은 반복문 안의 todo의 completed와 동기화 시켜준다.





app.$el을 콘솔에 입력하면 app 전체를 가져온다.

```html
<div id="app">…</div>
```

app.$el.firstChild은 div app에서 첫번째 차일드를 가져옴





npm init을 하면 패키지를 만들 수 있다(package.json에서 패키지에 대한 설정을 할 수 있다.)

npm install vue

npm i webpack webpack-cli -D

webpack.config.js 파일을 만든다.

```js
const path = require('path')

module.exports = {
  // entry: 여러개의 js파일의 시작점. 웹팩이 파일을 읽기 시작하는 지점
  entry: {},
  // module: 웹팩은 js만 변환이 가능하기 때문에 html, css같은 모듈을 통해서
  // 웹팩이 이해할 수 있는 것으로 변환을 해 주는 곳
  module: {},
  // plugins: 웹팩을 통해서 번들된 결과물을 추가적으로 처리하는 부분(옵션)
  plugins: [],
  // 여러 개의 js 파일을 하나로 만들어낸 결과물
  output: {},
}
```



$ touch src/main.js

```js
// 뷰 인스턴스를 최종적으로 만드는 파일
// 연결되어 있는 모든 js파일의 최상단에 존재하는 파일

// 1. npm install vue -> 추가
import Vue from 'vue'
// 2. 최상위 컴포넌트 ApplicationCache.vue를 추가(내가 만들 파일)
import App from './App.vue'
// 3. 뷰 인스턴스를 돔에 연결
new Vue({
  render : h => h(App),
}).$mount('#app'))


/*
new Vue({
  render function(createElement){
    return createElement(App)
  }
})
*/
```



$ touch src/App.vue

```vue
<template>
  <h1>여기는 최상위 컴포넌트</h1>
</template>

<script>

</script>

<style>

</style>
```



$ npm install vue-loader vue-template-compiler -D



$ npm run build





### vue cli

npm i -g @vue/cli

vue create todo-vue-cli   			(뷰 크리에이트 프로젝트명)

default 선택

이렇게 하고 나면 프로젝트명 폴더 안에서

npm run serve

하면 끝난다.