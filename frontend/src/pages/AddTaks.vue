<template>
  <div class="container-fluid" style="padding: 0">
    <Navbar/>
    <div class="row">
      <div class="col-8 mx-sm-auto p-4">

        <a href="/"><i class="fa fa-chevron-left" aria-hidden="true"></i> powrót</a>
        <hr/>
        <h3>Dadaj zadanie</h3>
        <hr/>

        <div v-if="addStatus == false" class="alert alert-warning text-center" role="alert" id="alert-invalid-data">
            <h4 class="alert-heading">❌ Nie udało się dodać zadania! ❌</h4>
            <hr>
            <p class="mb-0">Wypełnij wszystkie pola w poniższym formularzu</p>
        </div>

        <div v-if="addStatus == true" class="alert alert-success text-center" role="alert" id="alert-valid-data">
            <h4 class="alert-heading">✔️ Dodano zadanie! ✔️</h4>
        </div>

        <div class="col-lg-6 offset-lg-2">

            <table class="table table-hover text-left">
                <tr>
                    <td></td>
                    <th scope="row">Tytuł</th>
                    <td></td>
                    <td>
                        <input type="text" id="name" class="form-control" v-model="payload.title">
                    </td>
                </tr>
                <tr>
                    <td></td>
                    <th scope="row">Treść zadania</th>
                    <td></td>
                    <td>
                        <textarea class="form-control" v-model="payload.content"></textarea>
                    </td>
                </tr>
            </table>

            <br/>
            <div class="text-center">
                <button @click="add" type="button" class="btn btn-primary">Dodaj</button>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { taskService } from '../services';
import Navbar from '../components/Navbar';

export default {
  name: 'AddTaks',
  components: { Navbar },
  data () {
        return {
            addStatus: null,
            payload: {
                title: null,
                content: null,
                user: JSON.parse(localStorage.getItem('user')).id
            },
        }
    },
  methods: {
    add() {
      if (! this.validatePayload()) {
        this.addStatus = false;
        return;
      }
      taskService.addTask(this.payload)
        .then(response => {
          console.log(response);
          this.addStatus = response.status == 201 ? true : false;
      }).catch(() => this.addStatus = false);
    },
    validatePayload() {
      return (this.payload.title != null && this.payload.title.length > 0)
        && (this.payload.content != null && this.payload.content != '')
    },
  }
}
</script>