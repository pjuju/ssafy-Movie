<template>
  <div class="movie-list">
  <!-- <b-carousel
    id="carousel-fade"
    style="text-shadow: 0px 0px 2px #000 ; width:40%; height:40%;"
    fade
    :indicators="true"
    :interval="4000"

  >
  <div v-for=" movie in randomMovie" :key="movie.id">
    <b-carousel-slide
      :img-src="'https://image.tmdb.org/t/p/w500'+ movie.backdrop_path"
    ></b-carousel-slide>
  </div>
  </b-carousel> -->


  <div v-if="isLoggedIn">
  
    <div v-if="likeMoviesLength">
    <p class="d-flex justify-content-start ms-3 fs-4">내가 찜한 영화</p>
    <div v-if="likeMoviesLength >= 8">
      <vue-glide 
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="slider"
        :bound="true"
        :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 4}, 1000: {perView: 2} }"
        :gap="10">
        <vue-glide-slide v-for="movie in likeMovies" :key="movie.id">
          <movie-card :movie="movie" />
        </vue-glide-slide>
      </vue-glide>
    </div>

    <div class="d-flex justify-content-start" v-if="likeMoviesLength < 8">
      <div id="littlecount" v-for="movie in likeMovies" :key="movie.id">
        <div class="me-4">
          <movie-card :movie="movie" />
        </div>
      </div>
    </div>
    <hr>
    </div>
    

    <div v-if="likeWatchedLength">
    <p class="d-flex justify-content-start ms-3 fs-4">내가 본 영화와 비슷한 영화 </p>
    <div v-if="likeWatchedLength >= 8">
      <vue-glide 
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="slider"
        :bound="true"
        :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 4}, 1000: {perView: 2} }"
        :gap="10">
        <vue-glide-slide v-for="movie in likeWatched" :key="movie.id">
            <movie-card :movie="movie" />
        </vue-glide-slide>
      </vue-glide>
    </div>
    <div class="d-flex justify-content-start" v-if="likeWatchedLength < 8">
      <div id="littlecount" v-for="movie in likeWatched" :key="movie.id">
        <div class="me-4">
          <movie-card :movie="movie" />
        </div>
      </div>
    </div>
    <hr>
    </div>


    <div v-if="genderMoviesLength">
    <p class="d-flex justify-content-start ms-3 fs-4">내 성별이 좋아하는 영화</p>
    <div v-if="genderMoviesLength >= 8">
      <vue-glide 
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="slider"
        :bound="true"
        :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 4}, 1000: {perView: 2} }"
        :gap="10">
        <vue-glide-slide v-for="movie in genderMovies" :key="movie.id">
          <movie-card :movie="movie" />
        </vue-glide-slide>
      </vue-glide>
    </div>
    <div class="d-flex justify-content-start" v-if="genderMoviesLength < 8">
      <div id="littlecount" v-for="movie in genderMovies" :key="movie.id">
        <div class="me-4">
          <movie-card :movie="movie" />
        </div>
      </div>
    </div>
    <hr>
    </div>

  <div v-if="ageMoviesLength">
    <p class="d-flex justify-content-start ms-3 fs-4">또래들이 좋아하는 영화</p>
    <div v-if="ageMoviesLength >= 8">
      <vue-glide 
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="slider"
        :bound="true"
        :breakpoints="{ 3500: {perView: 7}, 1500: {perView: 4}, 1000: {perView: 2} }"
        :gap="10">
        <vue-glide-slide v-for="movie in ageMovies" :key="movie.id">
          <movie-card :movie="movie" />
        </vue-glide-slide>
      </vue-glide>
    </div>
    <div class="d-flex justify-content-start" v-if="ageMoviesLength < 8">
      <div id="littlecount" v-for="movie in ageMovies" :key="movie.id">
        <div class="me-4">
          <movie-card :movie="movie" />
        </div>
      </div>
    </div>
    </div>
    <hr>
    </div>


  <div v-if="followMoviesLength">
    <p class="d-flex justify-content-start ms-3 fs-4">내 팔로우가 좋아하는 영화</p>
    <div v-if="followMoviesLength >= 8">
      <vue-glide 
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="slider"
        :bound="true"
        :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 4}, 1000: {perView: 2} }"
        :gap="10">
        <vue-glide-slide v-for="movie in followMovies" :key="movie.id">
          <movie-card :movie="movie" />
        </vue-glide-slide>
      </vue-glide>
    </div>
    <div class="d-flex justify-content-start" v-if="followMoviesLength < 8">
      <div id="littlecount" v-for="movie in followMovies" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>
    <hr>
    </div>

    
    <p class="d-flex justify-content-start ms-3 fs-4">지금 인기있는 영화</p>
    <vue-glide v-if="popular.length > 8"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="slider"
      :bound="true"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 4}, 800: {perView: 2} }"
      :gap="10">
      <vue-glide-slide v-for="movie in popular" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>
    <div v-if="popular.length <= 8">
      <div v-for="movie in popular" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>
    <hr>



    <p class="d-flex justify-content-start ms-3 fs-4">출시 예정 영화</p>
    <vue-glide v-if="upComing.length > 8"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="slider"
      :bound="true"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 4}, 1000: {perView: 2} }"
      :gap="10">
      <vue-glide-slide v-for="movie in upComing" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>
    <div v-if="upComing.length <= 8">
      <div v-for="movie in upComing" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>    
    <hr>

    <p class="d-flex justify-content-start ms-3 fs-4">현재 상영 중인 영화</p>
    <vue-glide v-if="nowPlaying.length >= 8"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="slider"
      :bound="true"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 4}, 1000: {perView: 2} }"
      :gap="10">
      <vue-glide-slide v-for="movie in nowPlaying" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>
    <div v-if="nowPlaying.length < 8">
      <div v-for="movie in nowPlaying" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>
    


  </div>
</template>

<script>


import MovieCard from '@/components/MovieCard.vue'
import _ from 'lodash'
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
    ...mapGetters(['popular', 'nowPlaying', 'upComing', 'likeMovies', 'likeWatched', 'topRated',
    'genderMovies', 'ageMovies', 'followMovies', 'isLoggedIn' ]),
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
    randomMovie(){
      return _.sampleSize(this.topRated, 3)    
    }


  },
  methods:{
    ...mapActions([
      'fetchPopularMovies', 'fetchNowPlayingMovies','fetchLikeMovies', 'fetchLikeWatched', 'fetchTopRated',
      'fetchGenderMovies', 'fetchAgeMovies', 'fetchUpcomingMovies', 'fetchFollowMovies']),
      getHome(){
        if(this.isLoggedIn){
          this.fetchLikeMovies()
          this.fetchLikeWatched()
          this.fetchGenderMovies()
          this.fetchAgeMovies()
          this.fetchFollowMovies()
        }
      }
  
  },
  // likemovie, likewatchmovie, usergendermovie, useragemovie, upcoming, followmovie
  created(){
    this.fetchPopularMovies()
    this.fetchNowPlayingMovies()
    this.fetchUpcomingMovies()
    this.fetchTopRated()
    this.getHome()
  },
}
</script>

<style>

</style>