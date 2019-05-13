<template>
  <div id="app">
    <dyn-form></dyn-form>
  </div>
</template>

<script>
import DynForm from './components/DynForm.vue'

export default {
  name: 'app',
  components: {
    DynForm
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
