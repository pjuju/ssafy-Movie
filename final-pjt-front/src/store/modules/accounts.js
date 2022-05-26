import drf from '@/api/drf'
import router from '@/router'
import axios from 'axios'

export default {
  state:{
    token: localStorage.getItem('token') || '',
    currentUser:{},
    authError: null,
    profileUser:{},
  },
  getters:{
    isLoggedIn: state => !!state.token,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    authError: state => state.authError,
    currentUser: state => state.currentUser,
    currentUsername: state=> state.currentUser.username,
    profileUser: state => state.profileUser
  },
  mutations:{
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_TOKEN: (state, token) => state.token = token,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_PROFILE_USER: (state, user) => state.profileUser = user,

  },
  actions:{
    removeToken({ commit }){
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')

    },
    saveToken({ commit }, token){
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },
    // 회원가입
    signup({ commit, dispatch }, credentials){
      axios({
        method: 'POST',
        url: drf.accounts.signup(),
        data: credentials
      })
      .then(res=>{
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        router.push({ name: 'movies'})
      })
      .catch(err=> {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })

    },
    // 로그인
    login({commit, dispatch}, credentials){
      axios({
        method: 'post',
        url: drf.accounts.login(),
        data: credentials
      })
      .then(res => {
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        router.push({ name: 'movies'})
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    // 로그아웃
    logout({getters, dispatch}){
      axios({
        method: 'POST',
        url: drf.accounts.logout(),
        headers: getters.authHeader
      })
      .then(() => {
        dispatch('removeToken')
      })
      .catch(err =>{
        console.error(err.response)
      })
    },

    // 사용자 로그인상태 확인
    fetchCurrentUser({commit, getters, dispatch}){
      if (getters.isLoggedIn){
        axios({
          method: 'get',
          url: drf.accounts.currentUserInfo(),
          headers: getters.authHeader,
        })
        .then(res =>{
          commit('SET_CURRENT_USER', res.data)})
        .catch(err =>{
          if (err.response.status === 401 ) {
            dispatch('removeToken')
            router.push({ name: 'login' })
          }
        })
      }
    },

    // 프로필 유저 업데이트
    fetchProfileUser({commit}, username){
      axios({
        method: 'get',
        url: drf.accounts.profile(username),        
      })
      .then(res =>{
        commit('SET_PROFILE_USER', res.data)})
      .catch(err =>{
        console.error(err.response)
      })
    },
    follow({getters, dispatch}, username){      
      axios({
        method:'post',
        url: drf.accounts.follow(username),        
        headers: getters.authHeader,
      })
      .then(()=>{
        dispatch('fetchProfileUser', username)
      })
      .catch(err =>
        console.log(err.response))
    },
    
  },
  
}