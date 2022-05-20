<template>
    <div>
        <table class="table table-hover text-center">
            <thead v-if="showTableHead">
            <tr>
                <th scope="col" style="width: 33%">Tytuł</th>
                <th scope="col" style="width: 33%">Stan</th>
                <th scope="col" style="width: 33%">Akcje</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="todo in todos" :key="todo.id">
                <td style="width: 33%">{{ todo.title }}</td>
                <td style="width: 33%">
                    <div v-if="todo.completed" class="badge badge-pill badge-success" style="font-size: 20px">Ukończone</div>
                    <div v-else class="badge badge-pill badge-danger" style="font-size: 20px">Nie skończone</div>
                </td>
                <td style="width: 33%">
                    <button v-if="showTableHead" class="btn btn-success text-white" @click="markAsDone(todo.id)"><i class="fa fa-check-square-o"></i></button>
                    <a class="btn btn-primary text-white mx-1" v-bind:href="'/zadanie/' + todo.id"><i class="far fa-eye"></i></a>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import { taskService } from '../services';

export default {
    name: 'TaskTable',
    props: {
        todos: Array,
        showTableHead: Boolean
    },
    methods: {
        markAsDone(id) {
            console.log(`updating todo id: ${id}`);
            taskService.updateTask(id)
            this.$router.go(0);
        }
    }
}
</script>