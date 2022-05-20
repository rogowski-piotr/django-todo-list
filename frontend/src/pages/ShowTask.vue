<template>
  <div class="container-fluid" style="padding: 0">
    <Navbar/>
    <div class="row">
      <div class="col-8 mx-sm-auto p-4">
        <a href="/"><i class="fa fa-chevron-left" aria-hidden="true"></i> powrót</a>
        <hr/>
        <h3>Podgląd zadania</h3>
        <hr/>
        <div class="col-lg-6 offset-lg-2">
            <table class="table table-hover text-left">
                <tr>
                    <td></td>
                    <th scope="row">Tytuł</th>
                    <td></td>
                    <td colspan="2" v-if="task.title">{{ this.task.title }}</td>
                    <td colspan="2" v-else v-html="noDataLabel"></td>
                </tr>
                <tr>
                    <td></td>
                    <th scope="row">Treść zadania</th>
                    <td></td>
                    <td colspan="2" v-if="task.content">{{ this.task.content }}</td>
                    <td colspan="2" v-else v-html="noDataLabel"></td>
                </tr>
                <tr v-if="!task.completed && task.id">
                    <td></td>
                    <th scope="row">Oznacz jako ukończone</th>
                    <td></td>
                    <td colspan="2" v-if="task.content">
                      <button class="btn btn-success text-white" @click="markAsDone()"><i class="fa fa-check-square-o"></i></button>
                    </td>
                </tr>
            </table>
            <br/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { taskService } from '../services';
import Navbar from '../components/Navbar';

export default {
  name: 'ShowTask',
  components: { Navbar },
  data () {
      return {
          noDataLabel: '<small>brak danych 😥</small>',
          taskId: null,
          task: {
            id: null,
            title: null,
            content: null,
            completed: null,
            user: null,
          }
      }
  },
  created () {
      this.taskId = this.$route.params.id;
      taskService.fetchTask(this.taskId)
        .then(response => this.task = response)
  },
  methods: {
    markAsDone(id) {
        console.log(`updating todo id: ${id}`);
        taskService.updateTask(this.task.id);
        this.$router.go(0);
    }
  }
}
</script>