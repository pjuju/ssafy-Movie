<template>
  <div class="col">
    <div class="card h-100">
      <router-link class="text-decoration-none"
        :to="{ name: 'movie', params: {moviePk: review.movie.id} }">
      <img :src="poster" class="card-img-top" alt="img">
      </router-link>
       <router-link class="text-decoration-none text-black"
        :to="{ name: 'reviewDetail', params: { moviePk: review.movie.id, reviewPk: review.id } }">
      <div class="card-body">
     
        <p class="card-title fw-bold">
        <i style="color:red;" class="fa-solid fa-star"></i>
          {{review.rank}}</p>
          <h5 class="fw-bold">{{review.title}}</h5>
      
        <p class="card-text">
          {{review.content | cutLength}}
        </p>

        <i class="fa-solid fa-comment"></i> {{review.comments_count}}
        <i class="fa-solid fa-heart" style="color:red;"></i> {{likeCount}}
        <p>
        <small class="text-muted">{{review.user.username}}</small>
        </p>
        
      </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name:'ReviewListItem',
  props:{
    review:Object,
  },
  computed:{
    poster(){
      return 'https://image.tmdb.org/t/p/w500' + this.review.movie.poster_path
    },
    likeCount(){
      return this.review.like_users?.length
    }
  },
  filters:{
      cutLength(value){
        if(value.length > 30){
          return value.slice(0, 30) + '...'
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