<template>

<div>
    <div class="alert alert-success m-0" v-if="createdUser" role="alert" id="alert-incorrect-data">
        <h4 class="alert-heading">Zarejestrowano użytkownika!</h4>
    </div>
    <div class="alert alert-warning m-0" v-show="errorMessage != null" role="alert" id="alert-incorrect-data">
        <h4 class="alert-heading">Niepoprawne dane logowania!</h4>
    </div>
    <div class="bg-secondary vh-100"></div>

    <div class="modal fade show" aria-odal="true" style="display: block;">
        <div class="modal-dialog modal-login">
            <div class="modal-content bg-light">
                <div class="modal-header">				
                    <h4 class="modal-title">Formularz logowania</h4>
                </div>
                <div class="modal-body">
                    <div class="form-group">
                        <i class="fa fa-user p-1"></i>
                        <label>Nazwa użytkownika</label>
                        <input type="text" class="form-control" placeholder="Nazwa użytkownika" v-model="name"/>
                    </div>
                    <div class="form-group">
                        <i class="fa fa-lock p-1"></i>
                        <label>Hasło</label>
                        <input type="password" class="form-control" placeholder="Hasło" v-model="password"/>				
                    </div>
                    <div class="form-group">
                        <button @click="validateAuth" type="submit" class="btn btn-primary btn-block btn-lg">Zaloguj</button>
                    </div>
                </div>
                <div class="modal-footer">
                    <a href="/rejestracja">Zarejestruj się </a> jeśli nie masz konta w systemie
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import router from '../helpers/router';
import { userService } from '../services';

export default {
    name: 'Login',
    data() {
        return {
            name: null,
            password: null,
            errorMessage: null,
            createdUser: false,
        }
    },
    created () {
        userService.logout()
        this.createdUser = this.$route.query.createdUser;
    },
    methods: {
        validateAuth() {
            userService.login(this.name, this.password)
                .then(() => console.log('redirecting'))
                .then(router.push({path: "/"}))
                .then(() => window.location.href = '/')
                .catch(() => {
                    this.errorMessage = ' ';
                    this.createdUser = false;
                });
        },
    }
}
</script>