<template>
    <div>
        <table class="table table-hover text-center">
            <thead v-if="showTableHead">
            <tr>
                <th scope="col">Tytuł</th>
                <th scope="col">Stan</th>
                <th scope="col">Akcje</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="todo in todos" :key="todo.id">
                <td>{{ todo.title }}</td>
                <td>
                    <div v-if="todo.completed" class="badge badge-pill badge-success" style="font-size: 20px">Ukończone</div>
                    <div v-else class="badge badge-pill badge-danger" style="font-size: 20px">Nie skończone</div>
                </td>
                <td>
                    <button v-if="showTableHead" class="btn btn-info text-white" @click="markAsDone(todo.id)"><i class="fa fa-check-square-o"></i></button>
                    <a class="btn btn-primary text-white mx-1" v-bind:href="'/todo/' + todo.id"><i class="far fa-eye"></i></a>
                    <button class="btn btn-danger text-white" @click="deleteOne(todo.id)"><i class="far fa-trash-alt"></i></button>
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
        },
        deleteOne(id) {
        console.log(`deleting todo id: ${id}`);
        // taskService.delete(id)
        this.$router.go(0);
        }
    }
}
</script>