<template>
  <div class="container-fluid" style="padding: 0">
    <Navbar/>
    <div class="row">
      <div class="col-8 mx-sm-auto p-4">
        <h1>ADMIN</h1>
        <UserTable/>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Navbar';
import UserTable from '../components/UserTable';

export default {
  components: { Navbar, UserTable },
  name: 'Admin',
}
</script>