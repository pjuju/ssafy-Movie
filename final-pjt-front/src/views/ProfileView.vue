<template>
  <div>
    <div v-if="!profileUser.username">
      사용자가 존재하지 않습니다.
    </div>
    <div v-if="profileUser.username">
    <div class="d-flex justify-content-center align-items-center">
      <h2>{{profileUser.username}}님의 프로필</h2>
    </div>

    <div style="padding:0vw 20vw;">
    <div class="mb-3">
      <a class="text-white text-decoration-none" v-b-toggle href="#example-following" @click.prevent="changeCheck">팔로잉:{{followings}} </a>
      <a class="text-white text-decoration-none me-1" v-b-toggle href="#example-follower" @click.prevent="changeCheck">팔로워:{{followers}} </a>
    </div>
    <b-collapse id="example-following" v-if="followings && check">
      <b-card title="">
        <div v-for="following in profileUser.followings" :key="following.username">
          <router-link :to=" { name: 'profile', params: { username: following.username } }"  class="text-decoration-none text-black" >
            <p class="mb-0 text-black">{{following.username}}</p>
          </router-link>
        </div>
      </b-card>
    </b-collapse>
    <b-collapse id="example-follower" v-if="followers && check">
      <b-card title="">
        <div v-for="follower in profileUser.followers" :key="follower.username">

          <router-link :to=" { name: 'profile', params: { username: follower.username } }"  class="text-decoration-none text-black" >
            <p class="mb-0 text-black">{{follower.username}}</p>
          </router-link>
        </div>
      </b-card>
    </b-collapse>

    </div>
    <div v-if="profileUser.username !== currentUser.username">
      <i v-if="isLiked" @click="clickFollow" class="fa-solid fa-heart" style="color:red; cursor:pointer;"></i>
      <i v-if="!isLiked" @click="clickFollow" class="fa-regular fa-heart" style="color:red; cursor:pointer;"></i>
    </div>
    <hr>


    <div v-if="!likeMovies">
      <p class="text-start fs-4">찜한 영화가 없습니다</p>
    </div>

    <div v-if="likeMovies">
      <p class="d-flex justify-content-start fs-4">{{profileUser.username}}님이 찜한 영화</p>
      <div v-if="profileUser.like_movies.length >= 8">
        <vue-glide 
          class="glide__track"
          data-glide-el="track"
          ref="slider"
          type="slider"
          :bound="true"
          :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 4}, 1000: {perView: 3} }"
          :gap="10">
          <vue-glide-slide v-for="movie in profileUser.like_movies" :key="movie.id">
              <movie-card :movie="movie" />
          </vue-glide-slide>
        </vue-glide>
      </div>
      <div class="d-flex justify-content-start" v-if="profileUser.like_movies.length < 8">
        <div id="littlecount" v-for="movie in profileUser.like_movies" :key="movie.id">
          <div class="me-4">
            <movie-card :movie="movie" />
          </div>
        </div>
      </div>   
    </div> 
    <hr>

    <div v-if="!watchedMovies">
     <p class="text-start fs-4"> 시청한 영화가 없습니다.</p>
    </div>
    <div v-if="watchedMovies" >
      <p class="d-flex justify-content-start fs-4">{{profileUser.username}}님이 시청한 영화</p>
        <div v-if="profileUser.watched_movies.length >= 8">
          <vue-glide 
            class="glide__track"
            data-glide-el="track"
            ref="slider"
            type="carousel"
            :breakpoints="{ 3000: {perView: 8}, 1500: {perView: 5}, 1000: {perView: 2} }"
            :gap="10">
            <vue-glide-slide v-for="movie in profileUser.watched_movies" :key="movie.id">
                <movie-card :movie="movie" />
            </vue-glide-slide>
          </vue-glide>
        </div>
        <div class="d-flex justify-content-start" v-if="profileUser.watched_movies.length <= 8">
          <div id="littlecount" v-for="movie in profileUser.watched_movies" :key="movie.id">
            <div class="me-4">
              <movie-card :movie="movie" />
            </div>
          </div>
        </div>    
    </div>
    <hr>
    <div class="text-start" v-if="!reviewCount">
      <p class="fs-4">리뷰가 존재하지않습니다.</p>
    </div>
    <div v-if="reviewCount">
      <p class="d-flex justify-content-start fs-4">{{profileUser.username}}님의 리뷰</p>
      <div class="row row-cols-2 row-cols-md-4 row-cols-xl-6">
        <profile-review-item class="mb-4" v-for="review in profileUser.reviews" :key="review.id" :review="review"></profile-review-item>
      </div>
    </div>
    </div>
    
  </div>
</template>








<script>
import { mapActions, mapGetters } from 'vuex'
import { Glide, GlideSlide } from 'vue-glide-js'
import MovieCard from '@/components/MovieCard.vue'
import ProfileReviewItem from '@/components/ProfileReviewItem.vue'
export default {
  name:'ProfileView',
  components:{    
    MovieCard,
    ProfileReviewItem,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
  },
  data(){
    return{       
      isLiked: false,
      check: false,
    }
  },

  computed:{
    ...mapGetters(['profileUser', 'currentUser']),
    likeCount(){
      return this.profileUser.followers?.length      
    },
    getUsername(){
      return this.$route.params.username
    },
    followings(){
      return this.profileUser.followings?.length
    },
    followers(){
      return this.profileUser.followers?.length
    },
    reviewCount(){
      return this.profileUser.reviews?.length
    },
    watchedMovies(){
      return this.profileUser.watched_movies?.length
    },
    likeMovies(){
      return this.profileUser.like_movies?.length
    }
  },

  methods:{
    ...mapActions(['fetchProfileUser', 'follow']),
    onLike(){    
      const followers = JSON.parse(JSON.stringify(this.profileUser.followers)) 
                
      
      if (followers.some(user => user.id === this.currentUser.pk)){
      this.isLiked = true
      }
      else {this.isLiked = false}             
    },
    clickFollow(){      
      this.follow(this.getUsername)
    },
    changeCheck(){
      this.check = !this.check
    }
  },
  created(){
    this.fetchProfileUser(this.getUsername)
  },

  updated(){
    this.onLike()
  },
  watch: {
    $route(){
      this.changeCheck()
      this.fetchProfileUser(this.getUsername)
    }
  }
}
</script>

<style>

</style>