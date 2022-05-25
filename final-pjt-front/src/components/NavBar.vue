<template>
<div>
  <nav>
    <router-link :to=" { name: 'movies' }">HOME</router-link> |
    <div v-if="isLoggedIn">
      <router-link :to=" { name: 'review' }">REVIEW</router-link> |
      <button @click="logout"> 로그아웃 </button>
    </div>
    <!-- <router-link :to=" { name: 'profile', params: { username } }">프로필</router-link> | -->
    <div v-if="!isLoggedIn">
      <router-link :to=" { name: 'signup' }">회원가입</router-link> |
      <router-link :to=" { name: 'login' }">로그인</router-link> |
    </div>
  </nav>

</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'NavBar',
  methods:{
    ...mapActions(['logout']),
  },
  computed:{
    ...mapGetters(['isLoggedIn', 'currentUser']),
    // username(){
    //   return this.currentUser.username ? this.currentUser.username : 'guest'
    // },
  },
}
</script>

<style>

</style>
