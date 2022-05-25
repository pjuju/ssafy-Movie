<template>
  <div class="movie-list">

    <h1>POPULAR MOVIE</h1>
    <vue-glide v-if="popular.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
      :gap="10">
      <vue-glide-slide v-for="movie in popular" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>

    <h1>NOW PLAYING</h1>
    <vue-glide v-if="nowPlaying.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
      :gap="10">
      <vue-glide-slide v-for="movie in nowPlaying" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>

    <!-- likemovie, likewatchmovie, usergendermovie, useragemovie, upcoming, followmovie  -->

    <h1>Upcoming</h1>
    <vue-glide v-if="upComing.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
      :gap="10">
      <vue-glide-slide v-for="movie in upComing" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>

        <h1>내가 찜한 영화</h1>
    <vue-glide v-if="likeMovies.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
      :gap="10">
      <vue-glide-slide v-for="movie in likeMovies" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>

        <h1>내가 좋아요나 시청한 영화들과 비슷한 영화</h1>
    <vue-glide v-if="nowPlaying.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
      :gap="10">
      <vue-glide-slide v-for="movie in nowPlaying" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>

        <h1>내 연령대 유저들이 좋아요하거나 본 영화들</h1>
    <vue-glide v-if="nowPlaying.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
      :gap="10">
      <vue-glide-slide v-for="movie in nowPlaying" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>

        <h1>내 성별 유저들이 좋아요하거나 본 영화들</h1>
    <vue-glide v-if="nowPlaying.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
      :gap="10">
      <vue-glide-slide v-for="movie in nowPlaying" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>

        <h1>내 팔로우가 좋아요or본 영화</h1>
    <vue-glide v-if="nowPlaying.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
      :gap="10">
      <vue-glide-slide v-for="movie in nowPlaying" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>

  </div>
</template>

<script>


import MovieCard from '@/components/MovieCard.vue'
// import NowPlayingMovie from '@/components/NowPlayingMovie.vue'

import { Glide, GlideSlide } from 'vue-glide-js'
import { mapActions, mapGetters } from 'vuex'

export default {
  name:'MovieListView',
  components:{
    MovieCard,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide
  },
  computed:{
    ...mapGetters(['currentUser','popular', 'nowPlaying', 'upComing', 'likeMovies'])
  },
  methods:{
    ...mapActions([
      'fetchPopularMovies', 'fetchNowPlayingMovies','fetchLikeMovies', 'fetchLikeWatchedMovies',
      'fetchGenderMovies', 'fetchAgeMovies', 'fetchUpcomingMovies', 'fetchFollowMovies']),
  },
  // likemovie, likewatchmovie, usergendermovie, useragemovie, upcoming, followmovie
  created(){
    this.fetchPopularMovies()
    this.fetchNowPlayingMovies()
    this.fetchUpcomingMovies()
    this.fetchLikeWatchedMovies()
    this.fetchGenderMovies()
    this.fetchAgeMovies()
    this.fetchFollowMovies()
    this.fetchLikeMovies(this.currentUser.username)

  },
  mounted(){
  }
}
</script>

<style>

</style>