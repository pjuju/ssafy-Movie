<template>
  <div id="app">
    <nav-bar></nav-bar>
    <div class="padding">
      <router-view/>
      <footer-bar />
    </div>

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
@import url('https://fonts.googleapis.com/css2?family=Hahmlet:wght@500&display=swap');

#app {
  text-align: center;
  color: white;
  background-color: rgb(2, 3, 16);
  height: 100hv;
}

html { 
  background-color: rgb(2, 3, 16);
}

.padding {
  padding: 0vw 10vw;
  font-family: 'Hahmlet', serif;
  
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
