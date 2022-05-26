<template>
  <div v-if="review.user.username === currentUsername" class="col">
    <div class="card">
      <router-link class="text-decoration-none"
        :to="{ name: 'movie', params: {moviePk: review.movie.id} }">
      <img :src="poster" class="card-img-top" style="height:400px;" alt="img">
      </router-link>
       <router-link class="text-decoration-none text-white" style="background-color:rgba( 48, 47, 48)"
        :to="{ name: 'reviewDetail', params: { moviePk: review.movie.id, reviewPk: review.id } }">

      <div class="pt-1 card-body pb-0">
          <p>{{review.movie.title | cutTitle }}</p>
            <p class="fw-bold">{{review.title | cutTitle }}</p>      
          <div>
          <i v-for="i in review.rank" :key="i" style="color:orange;" class="fa-solid fa-star mb-3"></i>
          </div>
          <div>
          <i class="fa-solid fa-comment"></i> {{review.comments_count}}
          <i class="fa-solid fa-heart" ></i> {{likeCount}}
          </div>
      </div>
        <p class="text-muted pb-0">{{review.user.username}}</p>       


      </router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name:'ReviewListItem',
  props:{
    review:Object,
  },
  computed:{
    ...mapGetters(['currentUsername']),
    poster(){
      return 'https://image.tmdb.org/t/p/w500' + this.review.movie.poster_path
    },
    likeCount(){
      return this.review.like_users?.length
    }
  },
  filters:{
      cutLength(value){
        if(value.length > 50){
          return value.slice(0, 44) + '...'
        }
        else{
          return value
        }
      },
      cutTitle(value){
        if(value.length > 15){
          return value.slice(0, 15) + '...'
        }
        else{
          return value
        }
      }
  }
}
</script>

<style>

</style>