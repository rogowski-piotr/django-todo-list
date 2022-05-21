<template>

<div>
    <div class="alert alert-warning m-0" v-show="errorMessage != null" role="alert" id="alert-incorrect-data">
        <h4 class="alert-heading">Nie udało się zarejestrować!</h4>
        <hr>
        {{ errorMessage }}
    </div>
    <div class="bg-secondary vh-100"></div>

    <div class="modal fade show" aria-odal="true" style="display: block;">
        <div class="modal-dialog modal-login">
            <div class="modal-content bg-light">
                <div class="modal-header">				
                    <h4 class="modal-title">Formularz rejestracji</h4>
                </div>
                <div class="modal-body">
                    <div class="form-group">
                        <i class="fa fa-user p-1"></i>
                        <label>Nazwa użytkownika</label>
                        <input type="text" class="form-control" placeholder="Nazwa użytkownika" v-model="payload.username"/>
                    </div>
                    <div class="form-group">
                        <i class="fa fa-lock p-1"></i>
                        <label>Hasło</label>
                        <input type="password" class="form-control" placeholder="Hasło" v-model="payload.password"/>				
                    </div>
                    <div class="form-group">
                        <i class="fa fa-lock p-1"></i>
                        <label>Powtórz hasło</label>
                        <input type="password" class="form-control" placeholder="Hasło" v-model="repeatedPassword"/>				
                    </div>
                    <div class="form-group">
                        <button @click="tryRegister" type="submit" class="btn btn-primary btn-block btn-lg">Zarejestruj</button>
                    </div>
                </div>
                <div class="modal-footer">
                    <a href="/login">Zaloguj się</a> jeśli masz już konto
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import router from '../helpers/router';
import { userService } from '../services';
// import Login from '../pages/Login.vue';

export default {
  name: 'Login',
  data() {
    return {
        name: null,
        password: null,
        errorMessage: null,
        payload: {
            username: null,
            password: null,
        },
        repeatedPassword: null,
    }
  },
  created () {
        userService.logout()
    },
  methods: {
    tryRegister() {
        console.log('trying to register');
        if (this.validateRepeatedPassword()) {
            console.log('pass corected');
            userService.register(this.payload)
                .then(response => {
                    console.log(response);
                    if (response.status === 201) {
                        router.push({path: "/login?createdUser=true"});
                        window.location.href = '/login?createdUser=true';
                    } else {
                        this.errorMessage = ' ';
                    }
                })
                .catch(() => this.errorMessage = ' ')
        }
    },
    validateRepeatedPassword() {
        if (this.payload.username
            && this.payload.password
            && this.repeatedPassword
            && this.payload.password === this.repeatedPassword) {
            return true;
        }
        this.errorMessage = 'Wszystkie pola muszą być wypełnione a hasła identyczne';
        return false;
    }
  }
}
</script>