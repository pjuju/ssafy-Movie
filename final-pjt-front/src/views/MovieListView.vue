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

    <h1>NOW PLAYING</h1>
    <vue-glide v-if="nowPlaying.length > 7"
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
    <div v-if="nowPlaying.length <= 7">
      <div v-for="movie in nowPlaying" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>

    <div v-if="likeMoviesLength">
    <h1>내가 찜한 영화</h1>
    <div v-if="likeMoviesLength > 7">
      <vue-glide 
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
    </div>
    <div class="container" v-if="likeMoviesLength <= 7">
      <div id="littlecount" v-for="movie in likeMovies" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>
    </div>

    <div v-if="likeWatchedLength">
    <h1>like + watched</h1>
    <div v-if="likeWatchedLength > 7">
      <vue-glide 
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="carousel"
        :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
        :gap="10">
        <vue-glide-slide v-for="movie in likeWatched" :key="movie.id">
          <movie-card :movie="movie" />
        </vue-glide-slide>
      </vue-glide>
    </div>
    <div class="container" v-if="likeWatchedLength <= 7">
      <div id="littlecount" v-for="movie in likeWatched" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>
    </div>

    <div v-if="genderMoviesLength">
    <h1>gender movies</h1>
    <div v-if="genderMoviesLength > 7">
      <vue-glide 
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="carousel"
        :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
        :gap="10">
        <vue-glide-slide v-for="movie in genderMovies" :key="movie.id">
          <movie-card :movie="movie" />
        </vue-glide-slide>
      </vue-glide>
    </div>
    <div class="container" v-if="genderMoviesLength <= 7">
      <div id="littlecount" v-for="movie in genderMovies" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>
    </div>

  <div v-if="ageMoviesLength">
    <h1>AGE movies</h1>
    <div v-if="ageMoviesLength > 7">
      <vue-glide 
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="carousel"
        :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
        :gap="10">
        <vue-glide-slide v-for="movie in ageMovies" :key="movie.id">
          <movie-card :movie="movie" />
        </vue-glide-slide>
      </vue-glide>
    </div>
    <div class="container" v-if="ageMoviesLength <= 7">
      <div id="littlecount" v-for="movie in ageMovies" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>
    </div>

  <div v-if="followMoviesLength">
    <h1>FOLLOW movies</h1>
    <div v-if="followMoviesLength > 7">
      <vue-glide 
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="carousel"
        :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 5}, 1000: {perView: 3} }"
        :gap="10">
        <vue-glide-slide v-for="movie in followMovies" :key="movie.id">
          <movie-card :movie="movie" />
        </vue-glide-slide>
      </vue-glide>
    </div>
    <div class="container" v-if="followMoviesLength <= 7">
      <div id="littlecount" v-for="movie in followMovies" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>
    </div>


  </div>
</template>

<script>


import MovieCard from '@/components/MovieCard.vue'

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
    ...mapGetters(['popular', 'nowPlaying', 'upComing', 'likeMovies', 'likeWatched',
    'genderMovies', 'ageMovies', 'followMovies' ]),
    likeMoviesLength() {
      return this.likeMovies?.length
    },
    likeWatchedLength() {
      return this.likeWatched?.length
    },
    genderMoviesLength() {
      return this.genderMovies?.length
    },
    ageMoviesLength() {
      return this.ageMovies?.length
    },
    followMoviesLength() {
      return this.followMovies?.length
    },


  },
  methods:{
    ...mapActions([
      'fetchPopularMovies', 'fetchNowPlayingMovies','fetchLikeMovies', 'fetchLikeWatched',
      'fetchGenderMovies', 'fetchAgeMovies', 'fetchUpcomingMovies', 'fetchFollowMovies']),
  },
  // likemovie, likewatchmovie, usergendermovie, useragemovie, upcoming, followmovie
  created(){
    this.fetchPopularMovies()
    this.fetchNowPlayingMovies()
    this.fetchUpcomingMovies()
    this.fetchLikeMovies()
    this.fetchLikeWatched()
    this.fetchGenderMovies()
    this.fetchAgeMovies()
    this.fetchFollowMovies()


  },
}
</script>

<style>
/* #littlecount{
  display: inline-block;
} */

.container{
  display: flex;
  justify-content: center;
  margin: auto;
  flex-direction: row; 
}


</style>