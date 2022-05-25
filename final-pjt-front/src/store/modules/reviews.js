import drf from '@/api/drf'
import router from '@/router'
import axios from "axios"
import _ from 'lodash'

export default {
  state:{
    review: {},
    reviews: [],
  },
  getters:{
    review: state => state.review,
    reviews: state => state.reviews,
    isReview: state => !_.isEmpty(state.review),
    isAuthor: (state, getters) => {
      return state.review.user?.username === getters.currentUser.username
    }
  },
  mutations:{
    // SET_MOVIE_REVIEW: (state, review) => state.movie.reviews = review,
    SET_REVIEW:(state, review) => state.review = review,
    SET_REVIEWS:(state, reviews) => state.reviews = reviews,
  },
  actions:{
    createReview({getters}, payload){
      axios({
        method: 'post',
        url: drf.movies.reviews(payload.moviePk),
        data: payload,
        headers: getters.authHeader,
      })
      .then(res => {
        router.push({
          name: 'movie',
          params: { moviePk: res.data.movie.id }
        })
      })
      .catch(err => console.error(err.response))
    },
    updateReview({getters}, payload){
      axios({
        method: 'put',
        url: drf.movies.review(payload.moviePk, payload.reviewPk),
        data: payload,
        headers: getters.authHeader,
      })
      .then(res=>{
        router.push({
          name: 'reviewDetail',
          params:{
            moviePk: res.data.movie.id,
            reviewPk: res.data.id,
          }
        })
      })
      .catch(err => console.error(err.response))
    },
    deleteReview({commit, getters},{ moviePk, reviewPk}){
      if (confirm('삭제하시겠습니까?')){
      axios({
        method:'delete',
        url: drf.movies.review(moviePk, reviewPk),
        headers: getters.authHeader,
      })
      .then(()=>{
        commit('SET_REVIEW', {})
        router.go(-1)
      }) 
      }
    },
    fetchReview({commit, getters}, {moviePk, reviewPk}){
      axios({
        method: 'get',
        url: drf.movies.review(moviePk, reviewPk),
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_REVIEW', res.data)
      })
      .catch(err => {
        console.error(err.response)
        if (err.response.status === 404) {
          router.push({ name: 'NotFound404' })
        }
      })
    },
    fetchReviews({commit, getters}){
      axios({
        method: 'get',
        url: drf.movies.reviewList(),
        headers: getters.authHeader,
      })
      .then(res =>
        commit('SET_REVIEWS', res.data)
      )
      .catch(err =>{
        if (err.response.status === 401 ) {
          alert('로그인이 필요합니다.')
          router.push({ name: 'login' })
        }
      })
    },
    createComment({getters, dispatch}, {moviePk, reviewPk, content}){
      const comment = {content}
      axios({
        method:'post',
        url: drf.movies.comments(moviePk, reviewPk),
        data: comment,
        headers: getters.authHeader,
      })
      .then(()=>{
        const pk = {
          moviePk,
          reviewPk
        }
        dispatch('fetchReview', pk)
      })
      .catch(err =>
        console.log(err.response))
    },
    updateComment({getters, dispatch}, {moviePk, reviewPk, commentPk, content}){
      const comment = {content}
      axios({
        method: 'put',
        url: drf.movies.comment(moviePk, reviewPk, commentPk),
        data: comment,
        headers: getters.authHeader,
      })
      .then(()=>{
        const pk ={
          moviePk,
          reviewPk
        }
        dispatch('fetchReview', pk)
      })

    },
    deleteComment({getters, dispatch}, {moviePk, reviewPk, commentPk}){
      if (confirm('댓글을 삭제하시겠습니까?')){
        axios({
          method: 'delete',
          url: drf.movies.comment(moviePk, reviewPk, commentPk),
          data: {},
          headers: getters.authHeader,
        })
        .then(() => {
          const pk ={
            moviePk,
            reviewPk
          }
          dispatch('fetchReview', pk)
        })
      }
    },
    likeReview({getters, dispatch}, {moviePk, reviewPk}){    
      axios({
        method:'post',
        url: drf.movies.reviewlike(moviePk, reviewPk),        
        headers: getters.authHeader,
      })
      .then(()=>{
        dispatch('fetchReview', {moviePk, reviewPk})
      })
      .catch(err =>
        console.log(err.response))
    },
  }
}