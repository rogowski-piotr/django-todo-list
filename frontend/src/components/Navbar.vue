<template>
    <nav class="navbar navbar-light sticky-top bg-secondary flex-md-nowrap p-0 shadow">
        <a style="color: white" class="navbar-brand col-sm-3 col-md-2 mr-0 ml-5" href="#">Aplikacja - Lista zadań</a>
        <span class="navbar-text">
            <router-link to="/login" style="color: white" class="nav-link mr-5">Wyloguj mnie</router-link>
        </span>
    </nav>
</template>

<script>
export default {
    name: 'Navbar',
    data () {
        return {
            user: {}
        }
    },
    created () {
      this.user = JSON.parse(localStorage.getItem('user'));
    }
}
</script>