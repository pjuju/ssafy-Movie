<template>
  <div>
    <div class="movie-detail" v-if="movie.backdrop_path">
      <div class="movie-background" :style="{ backgroundImage: `url(${moviebackimgUrl})`}" style="background-size:cover">
        <div class="movie-content d-flex justify-content-center">
          <img class="p-4" :src="movieimgUrl" alt="">
          <div class="movie-text ms-3" style="width:800px">
            <div class="d-flex justify-content-between pt-4"><h1>{{movie.title}}</h1>
              <div class="d-flex align-items-center fs-3">
                <i v-if="isLiked" @click="clickLike" class="fa-solid fa-heart p-1" style="color:red; cursor:pointer;"></i>
                <i v-if="!isLiked" @click="clickLike" class="fa-regular fa-heart p-1" style="color:red; cursor:pointer;"></i>
                <i v-if="!isWatched" @click="clickWatch" class="fa-solid fa-eye p-1" style="cursor:pointer; "></i>
                <i v-if="isWatched" @click="clickWatch" class="fa-solid fa-eye-slash p-1" style="cursor:pointer;"></i>
              </div>
            </div>
            <p v-show="movie.tagline" class="text-start ps-2">"{{movie.tagline}}"</p>
            <hr>
            <div class="d-flex justify-content-start ps-2">
            <span class="genres" v-for="genre in movie.genres" :key="genre.id">{{genre.name}}</span>
            </div>
            <div class="text-start ps-2">
              <span>{{movie.release_date}} | {{movie.runtime}}분</span>
              <div class="fs-5">     
                <p class="pt-4">{{movie.overview}}</p>
              </div>
            </div>
            <div class="d-flex justify-content-center align-items-center mt-4" v-if="videoUrl">
              <div class="ratio ratio-16x9 ms-2 mb-4">
                <iframe :src="videoUrl" title="YouTubevideo" allowfullscreen></iframe>
              </div>
            </div>
            
          </div>      
        </div>
      </div>
    </div>
    <hr>
    <div class="text-start">
      <router-link :to="{name: 'review'}" class="text-decoration-none text-white">
        <h4>Review</h4>
      </router-link>
      <div v-if="!isLoggedIn">
      <p class="mb-0"> 리뷰를 보려면 로그인이 필요합니다.</p>
      </div>
      <div v-if="isLoggedIn">
        <p>리뷰 수: {{movie.review_count}}</p>
        <i class="fa-solid fa-pen-to-square pb-4" @click="reviewNew">리뷰쓰기</i>
      <br>
      <div v-if="movie.review_count > 5">
        <vue-glide 
          class="glide__track"
          data-glide-el="track"
          ref="slider"
          type="slider"
          :breakpoints="{ 3000: {perView: 5}, 1500: {perView: 3}, 1000: {perView: 2} }"
          :bound="true"
          :gap="10">
          <vue-glide-slide v-for="review in manyLikeReviews" :key="review.pk">
            <div class="card mb-0 col border-light mx-3" style="max-width: 18rem;">
              <div class="card-header d-flex justify-content-between align-items-center"
              style="background-color: rgba( 211, 211, 211)">
                  <div>
                    <i class="fa-solid fa-user me-1"></i>
                    <span class="text-black">{{review.user.username}}</span>
                  </div>
                  <div class="rank-border">
                    <i style="color:orange;" class="fa-solid fa-star"></i>
                    {{review.rank}}
                  </div>
                </div>
                    <router-link :to="{name: 'reviewDetail', params: {moviePk: movie.id, reviewPk: review.id} }" 
                      class="text-decoration-none text-black"
                      style="background-color: rgba( 211, 211, 211)">
                    <div class="card-body text-start pb-0">
                      <h5 class="card-title">{{review.title | cutTitle}}</h5>
                        <p class="card-text">{{review.content | cutLength}}</p>
                        <hr>
                        <div>
                          <div class="d-flex align-items-center heart-comment">
                            <small>
                            <i class="fa-solid fa-comment" style="color:blue;"></i> {{review.comments_count}}
                            <i class="fa-solid fa-heart" style="color:red;"></i> {{review.like_users.length}}
                            </small>
                          </div>
                          <p><small class="text-muted">{{review.created_at | cutDate}}</small></p>
                        </div>
                    </div>
                    </router-link>            
            </div>
          </vue-glide-slide>
        </vue-glide>
      </div>    <div v-if="movie.review_count <= 5" class="row">
      <div v-for="review in manyLikeReviews" :key="review.pk"
       class="card p-0 mb-0 col border-light mx-3" style="max-width: 18rem;">
        <div class="card-header d-flex justify-content-between align-items-center"
        style="background-color: rgba( 211, 211, 211)">
          <div>
            <i class="fa-solid fa-user me-1"></i>
            <span class="text-black me-1"> <router-link class="text-decoration-none text-black" :to="{ name:'profile', params:{ username: review.user.username} }">
            {{review.user.username}}</router-link></span>
          </div>
          <div class="rank-border">
            <i style="color:orange;" class="fa-solid fa-star"></i>
            {{review.rank}}
          </div>
        </div>
      <router-link :to="{name: 'reviewDetail', params: {moviePk: movie.id, reviewPk: review.id} }" 
        class="text-decoration-none text-black"
        style="background-color: rgba( 211, 211, 211)">
      <div class="card-body text-start pb-0">
        <h5 class="card-title">{{review.title | cutTitle}}</h5>
          <p class="card-text">{{review.content | cutLength}}</p>
          <hr>
          <div>
            <div class="d-flex align-items-center heart-comment">
              <small>
              <i class="fa-solid fa-comment" ></i> {{review.comments_count}}
              <i class="fa-solid fa-heart"></i> {{review.like_users.length}}
              </small>
            </div>
            <p><small class="text-muted">{{review.created_at | cutDate}}</small></p>
          </div>
      </div>
      </router-link>
      </div>
    </div>
    </div>
    </div>
    <hr>
    <p class="d-flex justify-content-start ms-3 fs-4">{{movie.title}} 관련 영화</p>
    <vue-glide v-if="similarMovies.length >= 8"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="slider"
      :bound="true"
      :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 4}, 1000: {perView: 2} }"
      :gap="10">
      <vue-glide-slide v-for="movie in similarMovies" :key="movie.id">
        <movie-card :movie="movie" />
      </vue-glide-slide>
    </vue-glide>
    <div v-if="similarMovies.length < 8">
      <div v-for="movie in similarMovies" :key="movie.id">
        <movie-card :movie="movie" />
      </div>
    </div>
    
  </div>
  
</template>

<script>

// 리뷰가져와서 타이틀만 뽑아서 나열해야함

import { mapActions, mapGetters } from 'vuex'
import _ from 'lodash'
import MovieCard from '@/components/MovieCard.vue'

import { Glide, GlideSlide } from 'vue-glide-js'

export default {
  name:'MovieDetailView',
  data(){
    return{
      moviePk: this.$route.params.moviePk,
      isLiked: false,
      isWatched: false,
    }
  },
  components:{
    MovieCard,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide
  },
  computed:{
    ...mapGetters(['movie', 'movieimgUrl', 'moviebackimgUrl',
     'isLoggedIn','currentUser', 'videoUrl','similarMovies']),
    manyLikeReviews(){
      return _.sortBy(this.movie.reviews, 'like_users_count').reverse()
    }

  },
  methods:{
    ...mapActions(['fetchMovie', 'likeMovie', 'watchMovie', 'fetchVideo','fetchSimilar']),
    reviewNew(){
      this.$router.push({name: 'reviewNew', params: {moviePk: this.movie.id}})
    },
    onLike(){            
      const like_users = JSON.parse(JSON.stringify(this.movie.like_users))
      if (like_users.some(user => user.pk === this.currentUser.pk)){
        this.isLiked = true
      }
      else {this.isLiked = false}      
    },
    clickLike(){
      const moviePk = this.movie.id      
      this.likeMovie(moviePk)
    },

    onWatch(){            
      const like_users = JSON.parse(JSON.stringify(this.movie.watched_users))
      if (like_users.some(user => user.pk === this.currentUser.pk)){
        this.isWatched = true
      }
      else {this.isWatched = false}      
    },
    clickWatch(){
      const moviePk = this.movie.id      
      this.watchMovie(moviePk)
      // this.fetchMovie(moviePk)
    },


  },
  created(){
    console.log(this.$route.params.moviePk)
    this.fetchSimilar(this.$route.params.moviePk)
    this.fetchVideo(this.$route.params.moviePk)
    this.fetchMovie(this.$route.params.moviePk)
    
  },
  updated(){
    this.onLike()
    this.onWatch()
  },
  watch:{
    $route(){
      this.fetchSimilar(this.$route.params.moviePk)
      this.fetchMovie(this.$route.params.moviePk)
    }
  },


  filters : {  
    cutDate(value){
      const ymd = value.slice(0,10)
      const hm = value.slice(11,16)
      return ymd + ' ' + hm
    },
    cutLength(value){
      if(value.length > 50){
        return value.slice(0, 38) + '...'
      }
      else{
        return value
      }
    },
    cutTitle(value){
      if(value.length > 13){
        return value.slice(0, 8) + '...'
      }
      else{
        return value
      }
    }
  }
}
</script>

<style>
.movie-detail{
  padding: 20px 20px;
  color: white;
}
.movie-content{
  height: 100%;
  background-color: rgba( 40, 40, 40, 0.5 );
}
.genres:not(:first-of-type)::before{
  content: "/";
}

.card-text{
  height: 48px;
}
.fa-pen-to-square {
  cursor: pointer;
  color: white;
}
.list-group {
  margin: 0 auto; 
  width:60%;
}
.card {
  color: black;
}
.i-button{
  cursor:pointer;
}
.heart-comment{
  color: rgb(40, 40, 40);
}
.fa-eye{
  color:white;
}



</style>