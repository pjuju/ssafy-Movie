<template>
<div class="mb-4">
  <div>
    <b-navbar type="dark pt-3" class="justify-content-between align-items-center">
      <div>
      <h5 class="fw-bold"> 
          <router-link :to=" { name: 'movies' }" class="text-decoration-none">
            SSAFY
          </router-link>        
      </h5>
      </div>

      <div class="d-flex align-items-center search-margin">     
      <b-form @submit.prevent="search">
        <b-form-input id="input-1" v-model="title" placeholder="영화를 검색하세요.">       
        </b-form-input>
      </b-form>
      <i class="fa-solid fa-magnifying-glass p-2"></i>
      </div>
      
      
      <b-navbar-nav>
        <b-nav-item>
          <router-link :to=" { name: 'movies' }" class="text-decoration-none">
            MOVIES
          </router-link>
        </b-nav-item>
        <b-nav-item v-if="isLoggedIn">
          <router-link :to=" { name: 'review' }" class="text-decoration-none">REVIEWS</router-link>
        </b-nav-item>
        <b-nav-item v-if="!isLoggedIn">
          <router-link :to=" { name: 'signup' }" class="text-decoration-none">회원가입</router-link>
        </b-nav-item>
        <b-nav-item v-if="!isLoggedIn">
          <router-link :to=" { name: 'login' }" class="text-decoration-none">로그인</router-link>
        </b-nav-item>


        <!-- Navbar dropdowns -->
      <div v-if="isLoggedIn && currentUser.username">
        <b-nav-item-dropdown :text="currentUser.username" right>
          <b-dropdown-item>  
            <router-link :to=" { name: 'profile', params: { username: currentUser.username } }"  class="text-decoration-none text-black" >
              <p class="mb-0">내 정보</p></router-link>
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
  data(){
    return {     
      title: '',     
      }
    },  
  methods:{
    ...mapActions(['logout', 'fetchSearchList']),
    search(){   
      this.$router.push({name:'movieSearchList', params:{title:this.title}})  
      this.fetchSearchList(this.title) 
      this.title = ''
      
    }
  },
  computed:{
    ...mapGetters(['isLoggedIn', 'currentUser']),
  },
}
</script>

<style>
.search-margin{
  margin-left: 11rem;
  height: 3rem;
}
</style>
