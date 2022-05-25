<template>
  <div>
    <div class="movie-detail" v-if="movie.backdrop_path">
      <div class="movie-background" :style="{ backgroundImage: `url(${moviebackimgUrl})`}" style="background-size:cover">
        <div class="movie-content d-flex">
          <img class="p-4" :src="movieimgUrl" alt="">
          <div class="movie-text ms-3">
            <h1 class="d-flex justify-content-start pt-4">{{movie.title}}</h1>
            <p class="text-start ps-2">"{{movie.tagline}}"</p>
            <hr>
            <div class="d-flex justify-content-start ps-2">
            <span class="genres" v-for="genre in movie.genres" :key="genre.id">{{genre.name}}</span>
            </div>
            <div class="text-start ps-2" style="width:80%">
            <span>{{movie.release_date}} | {{movie.runtime}}분</span>           
            <p class="pt-4">{{movie.overview}}</p>
            <span>
              <span v-for="user in movie.like_users" :key="user.pk">
                <div>
                  <button v-if="user.username === currentUser.username">NO HEART</button>
                  <button v-else>HEART</button>
                </div>
              </span>
              <!-- <button @click="onLike">좋아요</button> -->
            </span>
            <button>이미시청</button>
            </div>
          </div>      
        </div>
      </div>
    </div>
    <hr>
    <div>
      <router-link :to="{name: 'review'}" class="text-decoration-none text-white">
        <h4>Review</h4>
      </router-link>
      <p>리뷰 수: {{movie.review_count}}</p>
      <div v-if="!isLoggedIn">
      <p> 리뷰를 보려면 로그인이 필요합니다.</p>
      </div>
      <div v-if="isLoggedIn">
        <i class="fa-solid fa-pen-to-square" @click="reviewNew">리뷰쓰기</i>
        <div>
          <i class="fa-solid fa-bookmark"></i>
          <p>여기</p>
        </div>
      </div>
      <div>
        <div v-for="review in movie.reviews" :key="review.pk">

          <ul class="list-group">
            <li class="list-group-item d-flex justify-content-between align-items-center">
              <span class="text-black">
                <i style="color:red;" class="fa-solid fa-star"></i>
                {{review.rank}}

            <router-link :to="{name: 'reviewDetail', params: {moviePk: movie.id, reviewPk: review.id} }" class="ms-2">
              {{review.title}}
            </router-link>
            </span>
              <span class="badge bg-primary rounded-pill">{{review.comments_count}}</span>
            </li>
          </ul>

       </div>
      </div>
      <div v-for="review in movie.reviews" :key="review.pk">
      <div class="card border-light mb-3" style="max-width: 18rem;">
  <div class="card-header">Header</div>
  <div class="card-body">
    <h5 class="card-title">Light card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
  </div>
</div>
      </div>
      
    </div>

  </div>
  <!-- movie -> likeuser -> currentuser -->

  
</template>

<script>

// 리뷰가져와서 타이틀만 뽑아서 나열해야함

import { mapActions, mapGetters } from 'vuex'

export default {
  name:'MovieDetailView',
  data(){
    return{
      moviePk: this.$route.params.moviePk,
      isLiked: '',
    }
  },
  computed:{
    ...mapGetters(['movie', 'movieimgUrl', 'moviebackimgUrl', 'isLoggedIn','currentUser'])
  },
  methods:{
    ...mapActions(['fetchMovie',]),
    reviewNew(){
      this.$router.push({name: 'reviewNew', params: {moviePk: this.movie.id}})
    },


  },
  created(){
    this.fetchMovie(this.moviePk)
  }
}
</script>

<style>
.movie-detail{
  padding: 20px 20px;
  color: white;
}
.movie-content{
  height: 100hv;
  background-color: rgba( 40, 40, 40, 0.5 );
}
.genres:not(:first-of-type)::before{
  content: "/";
}
i {
  cursor: pointer;
}
.list-group {
  margin: 0 auto; 
  width:60%;
}

</style>