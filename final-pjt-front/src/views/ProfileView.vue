<template>
  <div>
    <h1>{{profileUser.username}}님의 프로필</h1>
    <i v-if="isLiked" @click="clickFollow" class="fa-solid fa-heart" style="color:red; cursor:pointer;"></i>
    <i v-if="!isLiked" @click="clickFollow" class="fa-regular fa-heart" style="color:red; cursor:pointer;"></i>

    <div v-if="profileUser.like_movies">
      <p class="d-flex justify-content-start ms-3 fs-4">{{profileUser.username}}님이 찜한 영화 : {{profileUser.like_movies.length}}개</p>
      <div v-if="profileUser.like_movies.length > 8">
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
      <div class="d-flex justify-content-start" v-if="profileUser.like_movies.length <= 8">
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
      username: this.$route.params.username,  
      isLiked: false,    
    }
  },

  computed:{
    ...mapGetters(['profileUser', 'currentUser']),
    likeCount(){
      return this.profileUser.followers?.length
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
    this.fetchProfileUser(this.username)
  },
  updated(){
    this.onLike()
  },
}
</script>

<style>

</style>