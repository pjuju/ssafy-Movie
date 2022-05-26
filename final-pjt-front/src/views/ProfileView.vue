<template>
  <div>
    <h1>{{profileUser.username}}님의 프로필</h1>
    <div> 
      팔로우: {{profileUser.followings.length}}
      팔로워: {{profileUser.followers.length}}
    </div>
    <div>팔로우 목록 
      <div v-for="following in profileUser.followings" :key="following.username">
        <router-link :to=" { name: 'profile', params: { username: following.username } }"  class="text-decoration-none text-black" >
          <p class="mb-0 text-white">{{following.username}}</p>
        </router-link>
      </div>
    </div>
    <div>팔로워 목록
      <div v-for="follower in profileUser.followers" :key="follower.username">
        <router-link :to=" { name: 'profile', params: { username: follower.username } }"  class="text-decoration-none text-black" >
          <p class="mb-0 text-white">{{follower.username}}</p>
        </router-link>
     </div>
    </div>
   
    <i v-if="isLiked" @click="clickFollow" class="fa-solid fa-heart" style="color:red; cursor:pointer;"></i>
    <i v-if="!isLiked" @click="clickFollow" class="fa-regular fa-heart" style="color:red; cursor:pointer;"></i>

    <div v-if="profileUser.like_movies">
      <p class="d-flex justify-content-start ms-3 fs-4">{{profileUser.username}}님이 찜한 영화 : {{profileUser.like_movies.length}}개</p>
      <div v-if="profileUser.like_movies.length >= 8">
        <vue-glide 
          class="glide__track"
          data-glide-el="track"
          ref="slider"
          type="carousel"
          :breakpoints="{ 3000: {perView: 8}, 1500: {perView: 5}, 1000: {perView: 3} }"
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

    <div v-if="profileUser.watched_movies">
      <p class="d-flex justify-content-start ms-3 fs-4">{{profileUser.username}}님이 시청한 영화 : {{profileUser.watched_movies.length}}개</p>
        <div v-if="profileUser.watched_movies.length > 8">
          <vue-glide 
            class="glide__track"
            data-glide-el="track"
            ref="slider"
            type="carousel"
            :breakpoints="{ 3000: {perView: 8}, 1500: {perView: 5}, 1000: {perView: 3} }"
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


    <div v-if="profileUser.reviews">
      <p class="d-flex justify-content-start ms-3 fs-4">{{profileUser.username}}님의 리뷰 : {{profileUser.reviews.length}}개</p>
      <div class="row row-cols-2 row-cols-md-4 row-cols-xl-6">
      <review-list-item class="mb-4" v-for="review in profileUser.reviews" :key="review.id" :review="review"></review-list-item>
      </div>
    </div>
    
    
  </div>
</template>








<script>
import { mapActions, mapGetters } from 'vuex'
import { Glide, GlideSlide } from 'vue-glide-js'
import MovieCard from '@/components/MovieCard.vue'
import ReviewListItem from '@/components/ReviewListItem.vue'
export default {
  name:'ProfileView',
  components:{    
    MovieCard,
    ReviewListItem,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
  },
  data(){
    return{       
      isLiked: false,    
    }
  },

  computed:{
    ...mapGetters(['profileUser', 'currentUser']),
    likeCount(){
      return this.profileUser.followers?.length      
    },
    getUsername(){
      return this.$route.params.username
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
      this.follow(this.username)
    },    
  },
  created(){
    this.fetchProfileUser(this.getUsername)
  },
  
  


  updated(){
    this.onLike()
    // this.fetchProfileUser(this.getUsername)
  },
}
</script>

<style>

</style>