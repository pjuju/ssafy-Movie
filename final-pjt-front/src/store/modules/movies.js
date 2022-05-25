import drf from '@/api/drf'
// import router from '@/router'
import axios from 'axios'

// const API_URL = 'https://api.themoviedb.org/3/movie/'
// const API_KEY = 'e97617d64b251b650b844ce38f163eaa'
// const params ={
//   api_key: API_KEY,
//   language : 'ko',
//   region : 'KR',

// }

export default {
  state:{
    movie: {},
    movieimgUrl: null,
    moviebackimgUrl: null,
    popular: {},
    nowPlaying: {},
    upComing:{},
    likeMovies:{},

    isLiked: null,
  },
  getters:{
    movie: state => state.movie,
    popular: state => state.popular,
    nowPlaying: state => state.nowPlaying,
    upComing: state => state.upComing,
    likeMovies: state => state.likeMovies,

    movieimgUrl: state => state.movieimgUrl,
    moviebackimgUrl: state => state.moviebackimgUrl,

  },
  mutations:{
    FETCH_POPULAR(state, movies){
      state.popular = movies      
    },
    SET_MOVIE(state, movie){
      state.movie = movie
      state.movieimgUrl = 'https://image.tmdb.org/t/p/w500'+ movie.poster_path
      state.moviebackimgUrl = 'https://image.tmdb.org/t/p/w500'+ movie.backdrop_path
    },
    FETCH_NOW_PLAYING(state, movies){
      state.nowPlaying = movies
    },
    FETCH_UPCOMING_MOVIES(state, movies){
      state.upComing = movies
    },
    FETCH_LIKE_MOVIES(state, movies){
      state.likeMovies = movies
    },

  },
  actions:{
    fetchPopularMovies({commit}){
      axios({
        method:'get',
        url: drf.movies.popular(),
      })
      .then(res=>{
        const popular = res.data.results
        commit('FETCH_POPULAR', popular)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },
    fetchNowPlayingMovies({commit}){
      axios({
        method:'get',
        url: drf.movies.nowPlaying(),
      })  
      .then(res=>{
        const nowPlaying = res.data.results
        commit('FETCH_NOW_PLAYING', nowPlaying)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },
    fetchUpcomingMovies({commit}){
      axios({
        method:'get',
        url: drf.movies.upcoming(),
      })  
      .then(res=>{
        commit('FETCH_UPCOMING_MOVIES', res.data.results)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },
    fetchLikeMovies({commit}, username){
      axios({
        method:'get',
        url: drf.movies.likemovies(username),
      })  
      .then(res=>{
        console.log(res.data.results)
        commit('FETCH_LIKE_MOVIES', res.data.results)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },
    fetchMovie({commit}, moviePk){
      axios({
        method:'get',
        url: drf.movies.movie(moviePk),
      })
      .then(res=>{
        const movie = res.data
        commit('SET_MOVIE', movie)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },
  },
}