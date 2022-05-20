<template>
  <div class="container-fluid" style="padding: 0">
    <Navbar/>
    <div class="row">
      <div class="col-8 mx-sm-auto p-4">
        <a class="btn btn-warning text-black my-2" v-bind:href="'/dodaj'">Dodaj zadanie</a>
        <TaskTable 
          v-bind:todos="todos.filter(todo => !todo.completed)"
          v-bind:showTableHead="true"/>
        <TaskTable 
          v-bind:todos="todos.filter(todo => todo.completed)"
          v-bind:showTableHead="false"/>
      </div>
    </div>
  </div>
</template>

<script>
import { taskService } from '../services';
import TaskTable from '../components/TaskTable';
import Navbar from '../components/Navbar';

export default {
  components: { TaskTable, Navbar },
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