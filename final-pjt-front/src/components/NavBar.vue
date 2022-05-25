<template>
<div class="mb-4">
  <div>
    <b-navbar type="dark" variant="dark" class="d-flex justify-content-start">
      <b-navbar-nav>
        <b-nav-item>
          <router-link :to=" { name: 'movies' }" class="text-decoration-none">
            HOME
          </router-link>
        </b-nav-item>
        <b-nav-item v-if="isLoggedIn">
          <router-link :to=" { name: 'review' }" class="text-decoration-none">REVIEW</router-link>
        </b-nav-item>
        <b-nav-item v-if="!isLoggedIn">
          <router-link :to=" { name: 'signup' }" class="text-decoration-none">회원가입</router-link>
        </b-nav-item>
        <b-nav-item v-if="!isLoggedIn">
          <router-link :to=" { name: 'login' }" class="text-decoration-none">로그인</router-link>
        </b-nav-item>


        <!-- Navbar dropdowns -->
        <div v-if="isLoggedIn">
        <b-nav-item-dropdown :text="currentUser.username" right>
          <b-dropdown-item>
            <router-link :to=" { name: 'review' }" class="text-decoration-none text-black">내 정보</router-link>
          </b-dropdown-item>
          <b-dropdown-item @click="logout" class="text-black">로그아웃</b-dropdown-item>
        </b-nav-item-dropdown>
        </div>
      </b-navbar-nav>
    </b-navbar>
  </div>
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
