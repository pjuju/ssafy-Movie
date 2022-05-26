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
    likeWatched:{},
    genderMovies:{},
    ageMovies:{},
    followMovies: {},
    isLiked: null,
    searchMovieList:{},
  },
  getters:{
    movie: state => state.movie,
    popular: state => state.popular,
    nowPlaying: state => state.nowPlaying,
    upComing: state => state.upComing,
    likeMovies: state => state.likeMovies,
    likeWatched: state => state.likeWatched,
    genderMovies: state => state.genderMovies,
    ageMovies: state => state.ageMovies,
    followMovies: state => state.followMovies,
    movieimgUrl: state => state.movieimgUrl,
    moviebackimgUrl: state => state.moviebackimgUrl,
    searchMovieList: state => state.searchMovieList,

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
    FETCH_LIKE_WATCHED(state, movies){
      state.likeWatched = movies
    },
    FETCH_GENDER_MOVIES(state, movies){
      state.genderMovies = movies
    },
    FETCH_AGE_MOVIES(state, movies){
      state.ageMovies = movies
    },
    FETCH_FOLLOW_MOVIES(state, movies){
      state.followMovies = movies
    },
    FETCH_SEARCH_MOVIES(state,movies){
      state.searchMovieList = movies
    }

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
        commit('FETCH_NOW_PLAYING', res.data.results)
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
    fetchLikeMovies({commit, getters}){
      axios({
        method:'get',
        url: drf.movies.likemovies(),
        headers: getters.authHeader,
      })  
      .then(res=>{
        commit('FETCH_LIKE_MOVIES', res.data)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },
    fetchLikeWatched({commit, getters}){
      axios({
        method:'get',
        url: drf.movies.likewatched(),
        headers: getters.authHeader,
      })  
      .then(res=>{
        commit('FETCH_LIKE_WATCHED', res.data)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },
    fetchGenderMovies({commit, getters}){
      axios({
        method:'get',
        url: drf.movies.gendermovies(),
        headers: getters.authHeader,
      })  
      .then(res=>{
        commit('FETCH_GENDER_MOVIES', res.data)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },
    fetchAgeMovies({commit, getters}){
      axios({
        method:'get',
        url: drf.movies.agemovies(),
        headers: getters.authHeader,
      })  
      .then(res=>{
        commit('FETCH_AGE_MOVIES', res.data)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },
    fetchFollowMovies({commit, getters}){
      axios({
        method:'get',
        url: drf.movies.followmovies(),
        headers: getters.authHeader,
      })  
      .then(res=>{
        commit('FETCH_FOLLOW_MOVIES', res.data)
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
    likeMovie({getters, dispatch}, moviePk){      
      axios({
        method:'post',
        url: drf.movies.likemovie(moviePk),        
        headers: getters.authHeader,
      })
      .then(()=>{
        dispatch('fetchMovie', moviePk)
      })
      .catch(err =>
        console.log(err.response))
    },    
    watchMovie({getters, dispatch}, moviePk){      
      axios({
        method:'post',
        url: drf.movies.watchedmovie(moviePk),        
        headers: getters.authHeader,
      })
      .then(()=>{
        dispatch('fetchMovie', moviePk)
      })
      .catch(err =>
        console.log(err.response))
    },
    fetchSearchList({commit}, title){
      axios({
        method:'get',
        url: drf.movies.serachmovies(title),
      })
      .then(res=>{
        commit('SET_SEARCH_MOVIES', res.data)
      })
      .catch(err=>{
        console.log(err.response)
      })
    },


  },
}