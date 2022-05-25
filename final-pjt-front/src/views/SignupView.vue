<template>
  <div v-if="!isLoggedIn">
    <account-error-list v-if="authError"></account-error-list>

    <h1>회원가입</h1>
    <b-form @submit.prevent="signup(credentials)">
      <b-form-group
        id="input-group-1"
        label="아이디"
        label-for="input-1"
        description="사용할 아이디를 입력하세요"
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
       description="비밀번호는 8자 이상으로 되어야 합니다.">
        <b-form-input
          id="input-2"
          v-model="credentials.password1"
          placeholder="PASSWORD"
          type="password"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="비밀번호 확인" label-for="input-3">
        <b-form-input
          id="input-3"
          v-model="credentials.password2"
          placeholder="PASSWORD"
          type="password"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-4" label="나이:" label-for="input-4">
        <b-form-select
        id="input-4"
        v-model="credentials.age"
        :options="ages"
        required></b-form-select>
      </b-form-group>
      <b-form-checkbox v-model="credentials.gender" value="male">남</b-form-checkbox>
      <b-form-checkbox v-model="credentials.gender" value="female">녀</b-form-checkbox>



      <b-button type="submit" variant="primary">회원가입</b-button>
    </b-form>


  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import _ from 'lodash'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name:'SignupView',
  components:{ AccountErrorList },
  data(){
    return{
      credentials:{
        username: '',
        password1: '',
        password2: '',
        age: '',
        gender: '',
      },
      ages: [{ text: 'Select One', value: null}, ..._.range(8,100)]
    }
  },
  computed:{
    ...mapGetters(['authError', 'isLoggedIn'])
  },
  methods:{
    ...mapActions(['signup'])
  }

}
</script>

<style>
form { 
  margin: 0 auto; 
  width:250px;
}
</style>