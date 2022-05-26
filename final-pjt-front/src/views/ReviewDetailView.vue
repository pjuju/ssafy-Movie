<template>
  <div>
    <div v-if="!isLoggedIn">
      <p>로그인이 필요합니다.</p>
    </div>
    <div v-if="isLoggedIn">
    <p class="text-muted">
      리뷰 | 
    <router-link
     :to="{ name: 'movie', params:{ moviePk: pk.moviePk } }"
      class="text-decoration-none">
      <span v-for="movie in review" :key="movie.id">
      <span v-if="movie.title" class="text-muted"> {{movie.title}}</span>
      </span>
    </router-link>
    </p>
    <div class="content">
        <h1>{{review.title}}</h1>
        <span> 작성자: </span>
        <router-link
        :to="{ name: 'profile', params:{ username: review.user.username } }"
          class="text-decoration-none">
      {{review.user.username}}
         </router-link>
      <span><small> {{review.updated_at | yyyyMMdd}}</small></span>  
    <hr>
      <!-- <div class="title-box">
      </div> -->


    <div v-if="review.user">                
    <div class="review-content" style="width:70%">
      <p> 내용:{{review.content}} </p>
    </div>
      <small>
        <span> 좋아요: {{likeCount}}개</span>
        <span> 댓글: {{review.comments_count}}개</span>
      </small>
    </div>
  </div>    
    <i v-if="isLiked" @click="clickLike" class="fa-solid fa-heart" style="color:red; cursor:pointer;"></i>
    <i v-if="!isLiked" @click="clickLike" class="fa-regular fa-heart" style="color:red; cursor:pointer;"></i>
    


    <div v-if="isAuthor">
      <button>
        <router-link :to="{name: 'reviewEdit', params: {moviePk: pk.moviePk, reviewPk: pk.reviewPk} }">
          EDIT
        </router-link>
      </button>
      <button @click="deleteReview(pk)">
        DELETE
      </button>
    </div>
    <hr>
    <h3>COMMENT</h3>
    
    <comment-list :comments="review.comments"></comment-list>
    <!-- <div v-for="comment in review.comments" :key="comment.id">
      {{comment.content}}
    </div> -->
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
      
      if (like_users.some(user => user.id === currentUser.pk)){
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
  }

}
</script>

<style>
.review-content{
  margin: auto;
}
.title-box{
  display: flex;
  justify-content: space-between;
  margin: auto;
  width:70%;
}
/* .content{
  display: flex;
  justify-content: center;
} */
</style>