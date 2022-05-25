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
          </div>      
        </div>
      </div>
    </div>



    <hr>
    <div>
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
      
      <div v-if="movie.review_count" class="row row-cols-1 row-cols-md-3 g-4">
      <div v-for="review in movie.reviews" :key="review.pk"
       class="card col border-light m-3" style="max-width: 18rem;">
      <div class="card-header">
        <i style="color:red;" class="fa-solid fa-star"></i>
          {{review.rank}}
          <small class="text-muted">{{review.user.username}}</small>
      </div>
      <router-link :to="{name: 'reviewDetail', params: {moviePk: movie.id, reviewPk: review.id} }" 
        class="text-decoration-none text-black">
      <div class="card-body">
      <h5 class="card-title">{{review.title}}</h5>
        <p class="card-text">{{review.content | cutLength}}</p>
        <div><i class="fa-solid fa-comment"></i> {{review.comments_count}} </div>
        <p><small class="text-muted">{{review.created_at | yyyyMMdd}}</small></p>
      </div>
      </router-link>
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
      isLiked: false,
      isWatched: false,
    }
  },
  computed:{
    ...mapGetters(['movie', 'movieimgUrl', 'moviebackimgUrl',
     'isLoggedIn','currentUser']),

  },
  methods:{
    ...mapActions(['fetchMovie', 'likeMovie', 'watchMovie']),
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
    this.fetchMovie(this.moviePk)
  },
  updated(){
    this.onLike()
    this.onWatch()
  },
  filters : {  
    yyyyMMdd(value){ 
            if(value == '') return '';
            
            var js_date = new Date(value);
            // 연도, 월, 일 추출
            var year = js_date.getFullYear();
            var month = js_date.getMonth() + 1;
            var day = js_date.getDate();

            if(month < 10){
              month = '0' + month;
            }

            if(day < 10){
              day = '0' + day;
            }

            return year + '-' + month + '-' + day;
    },
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
.fa-comment{
  color: rgb(25, 25, 179);
}
.fa-eye{
  color:white;
}

</style>