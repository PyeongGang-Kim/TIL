<template>
  <div>
  <h1>여기는 최상위 컴포넌트</h1>
  <TodoList category="취업준비"></TodoList>
  <TodoList category="SSAFY"></TodoList>
  <TodoList category="기타"></TodoList>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'
export default {
  components: {
    TodoList,
  }
}
</script>

<style>

</style>