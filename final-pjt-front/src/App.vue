<template>
  <div id="app">
    <nav-bar></nav-bar>
    <div class="padding">
    <router-view/>
    <br>
    <br>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import NavBar from '@/components/NavBar.vue'
import { mapActions } from 'vuex'

export default {
  name: 'App',
  components:{
    NavBar
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
  background-color: rgb(2, 3, 16);
  height: 100hv;
}

html { 
  background-color:rgb(2, 3, 16);
}

.padding {
  padding: 0vw 10vw;
  
}


nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
