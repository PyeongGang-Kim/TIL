// 뷰 인스턴스를 최종적으로 만드는 파일
// 연결되어 있는 모든 js파일의 최상단에 존재하는 파일

// 1. npm install vue -> 추가
import Vue from 'vue'
// 2. 최상위 컴포넌트 ApplicationCache.vue를 추가(내가 만들 파일)
import App from './App.vue'
// 3. 뷰 인스턴스를 돔에 연결
new Vue({
  render : h => h(App),
}).$mount('#app')



/*
new Vue({
  render function(createElement){
    return createElement(App)
  }
})
*/