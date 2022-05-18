<template>
  <div class="container-fluid">
    <div class="row">
      <h1>Dashboard</h1>
      </div>
      <TaskTable 
        v-bind:todos="todos.filter(todo => !todo.completed)"
        v-bind:showTableHead="true"/>
      <TaskTable 
        v-bind:todos="todos.filter(todo => todo.completed)"
        v-bind:showTableHead="false"/>
  </div>
</template>

<script>
import { taskService } from '../services';
import TaskTable from '../components/TaskTable'

export default {
  components: { TaskTable },
  name: 'Dashboard',
  data () {
    return { todos: [] }
  },
  created() {
    taskService.fetchTasks()
      .then(response => {
        console.log(response);
        this.todos = response;
      })
  },
}
</script>