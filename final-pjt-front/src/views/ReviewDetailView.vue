<template>
  <div class="review-box">
    <div v-if="!isLoggedIn">
      <p>
        <router-link :to="{name:'login'}">로그인</router-link>이 필요합니다.
      </p>
    </div>
    <div v-if="isLoggedIn && review.user">
    <p class="text-start text-muted">
      <router-link :to="{name:'review'}" class="text-decoration-none text-muted">
      리뷰
      </router-link> | 
    <router-link
     :to="{ name: 'movie', params:{ moviePk: pk.moviePk } }"
      class="text-decoration-none">
      <span v-for="movie in review" :key="movie.id">
      <span v-if="movie.title" class="text-muted"> {{movie.title}}</span>
      </span>
    </router-link>
    </p>
    <hr>
    <div class="content-title text-start">
      <h1>{{review.title}}</h1>
      <div class="d-flex justify-content-between">
        <span><small> 작성자: <router-link class="text-decoration-none text-white" :to="{ name:'profile', params:{ username: review.user.username} }">{{review.user.username}}</router-link></small></span>
        <span><small> {{review.updated_at | cutDate}}</small></span>  
      </div>
    <div v-if="isAuthor" class="d-flex justify-content-end align-items-center"> 
      <router-link :to="{name: 'reviewEdit', params: {moviePk: pk.moviePk, reviewPk: pk.reviewPk} }">
        <i class="fa-solid fa-pen-to-square me-1"></i>
      </router-link>      
      <i class="fa-solid fa-trash-can" style="cursor:pointer;" @click="deleteReview(pk)"></i>
    </div>      
    </div>
    <hr>

    <div class="content-content pb-4" v-if="review.user">
      <div class="text-start mb-2">
      <span><i style="color:yellow;" class="fa-solid fa-star"></i>
      <span>{{review.rank}}</span></span>
      </div>
      <h5 class="text-start" style="letter-spacing:0.5px;">{{review.content}} </h5>
    </div>
    <h5>
    <i v-if="isLiked" @click="clickLike" class="fa-solid fa-heart" style="color:red; cursor:pointer;"></i>
    <i v-if="!isLiked" @click="clickLike" class="fa-regular fa-heart" style="color:white; cursor:pointer;"></i>
    </h5>
    <small>
      <p> 좋아요: {{likeCount}}개</p>
    </small>
    <hr>
    <div class="comment-box">
    <p class="text-start"><small>댓글: {{review.comments_count}}개</small>
    </p>
    </div>
    
    <comment-list :comments="review.comments"></comment-list>

    <div>
      <comment-form></comment-form>
    </div>


  </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

import CommentList from '@/components/CommentList.vue'
import CommentForm from '@/components/CommentForm.vue'


export default {
  name:'ReviewDetailView',
  components:{
    CommentForm, CommentList
  },
  data(){
    return{
      pk:{ moviePk : this.$route.params.moviePk,
          reviewPk : this.$route.params.reviewPk
          },
      isLiked: false,

    }
  },
  computed:{
    ...mapGetters(['review', 'isAuthor','isLoggedIn', 'currentUser']),
    likeCount(){
      return this.review.like_users?.length
    }
  },
  methods:{
    ...mapActions(['fetchReview', 'deleteReview', 'likeReview']),
    onLike(){    
      const currentUser = JSON.parse(JSON.stringify(this.currentUser)) 
      const like_users = JSON.parse(JSON.stringify(this.review.like_users))           
      
      if (like_users.some(user => user.pk === currentUser.pk)){
      this.isLiked = true
      }
      else {this.isLiked = false}             
    },
    clickLike(){      
      this.likeReview(this.pk)
    },    
  },

  created(){
    this.fetchReview(this.pk)
  },
  updated(){
    this.onLike()
  },
  filters:{  
    cutDate(value){
      const ymd = value.slice(0,10)
      const hm = value.slice(11,16)
      return ymd + ' ' + hm
    },
  }

}
</script>

<style>
.review-box {
  padding: 0vw 10vw;  
}
/* .comment-box {
  border: 1px solid;
  border-radius: 30px;
} */
.rank-box{
  border: 1px solid;
  border-radius: 10px;
}
</style>