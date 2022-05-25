<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view/>
    <footer-bar></footer-bar>
  </div>
</template>

<script>
// import axios from 'axios'
import NavBar from '@/components/NavBar.vue'
import FooterBar from '@/components/FooterBar.vue'
import { mapActions } from 'vuex'

export default {
  name: 'App',
  components:{
    NavBar, FooterBar
  },
  methods:{
    ...mapActions(['fetchCurrentUser'])
  },
  created(){
    this.fetchCurrentUser()
  }

}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: rgb(34, 31, 31);
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
