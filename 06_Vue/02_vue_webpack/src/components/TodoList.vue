<template>
  <div class="todo-lists">
    <h2>{{ category }}</h2>
    <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
    <button v-on:click="addTodo">+</button>
    <li v-for="todo in todos" v-bind:key="todo.id">
      <span>{{todo.content}}</span>
      <button v-on:click="removeTodo(todo.id)">x</button>
    </li>
  </div>
  
</template>

<script>
export default{
  props: {
    // 카테고리 라는 속성의 유효성을 설정할 수 있다.
    // 유효성 벗어나도 동작은 하지만 오류가 발생함
    category: {
      type: String,
      required: true,
      validator: function(value){
        if (value.length < 15){
          return true
        } else {
          return false
        }
      }
    }
  },
  data: function() {
    return {
      todos: [],
      newTodo: '',
    }
  },
  methods: {
    addTodo: function() {
      if (this.newTodo.length !== 0){
        this.todos.push({
          id: Date.now(),
          content: this.newTodo,
          completed: false
        })
        this.newTodo = ''
      }
    }
  },
  removeTodo: function(todoId){
    this.todos = this.todos.filter((todo) => {
      return todo.id !== todoId
    })
  },
}
</script>

<style>
.todo-list {
  display: inline-block;
  width: 33%;
}

</style>