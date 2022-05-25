<template>
  <div v-if="!isLoggedIn" class="login-form">
    <account-error-list v-if="authError"></account-error-list>
    <b-form @submit.prevent="login(credentials)">
      <b-form-group
        id="input-group-1"
        label="아이디"
        label-for="input-1"
        description="아이디를 입력하세요"
      >
        <b-form-input
          id="input-1"
          v-model="credentials.username"
          placeholder="ID"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
       id="input-group-2"
       label="비밀번호"
       label-for="input-2"
       description="비밀번호를 입력하세요.">
        <b-form-input
          id="input-2"
          v-model="credentials.password"
          placeholder="PASSWORD"
          type="password"
          required
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">로그인</b-button>
    </b-form>


    <!-- <h1>Login</h1>
    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username"></label>
        <input type="text" v-model="credentials.username" id="username" required />
      </div>
      <div>
        <label for="password"></label>
        <input type="password" v-model="credentials.password" id="password" required />
      </div>
      <button>로그인</button>
    </form> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name:'LoginView',
  components:{
    AccountErrorList,
  },
  data(){
    return{
      credentials:{
        username: '',
        password: '',
      }
    }
  },
  computed:{
    ...mapGetters(['authError', 'isLoggedIn'])
  },
  methods:{
    ...mapActions(['login'])
  }

}
</script>

<style>
form { 
  margin: 0 auto; 
  width:250px;
}
.login-form{
  height:100%;
}
</style>