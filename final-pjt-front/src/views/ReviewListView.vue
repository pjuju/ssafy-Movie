<template>
  <div>
    <div v-if ="isLoggedIn && reviews.length ">
    <h1 class="text-start">리뷰</h1>
    <hr>
    <div class="d-flex justify-content-start mb-4">
    <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
      <input @click="normal= 1" type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
      <label class="btn btn-outline-secondary" for="btnradio1">최신</label>

      <input @click="normal= 2" type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
      <label class="btn btn-outline-secondary" for="btnradio2">인기</label>

      <input @click="normal= 3" type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
      <label class="btn btn-outline-secondary" for="btnradio3">내 글</label>
    </div>
    </div>
    
  <div v-if="normal===1">
    <div class="row row-cols-2 row-cols-md-3 row-cols-xl-5">
      <review-list-item class="mb-4" v-for="review in reviews" :key="review.id" :review="review"></review-list-item>
    </div>
  </div>
  <div v-if="normal===2">
    <div class="row row-cols-2 row-cols-md-3 row-cols-xl-5">
      <review-list-item class="mb-4" v-for="review in hotReviews" :key="review.id" :review="review"></review-list-item>
    </div>
  </div>
  <div v-if="normal===3">
    <div class="row row-cols-2 row-cols-md-3 row-cols-xl-5">
      <my-review-list-item class="mb-4" v-for="review in reviews" :key="review.id" :review="review"></my-review-list-item>
    </div>
  </div>
  </div>
  <div v-if="!isLoggedIn">
    <router-link :to="{name:'login'}">로그인</router-link>이 필요합니다.
  </div>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import ReviewListItem from '@/components/ReviewListItem.vue'
import MyReviewListItem from '@/components/MyReviewListItem.vue'
import _ from 'lodash'

export default {
  name:'ReviewListView',
  components:{ ReviewListItem, MyReviewListItem },
  data(){
    return{
      normal: 1,
    }
  },
  computed:{
    ...mapGetters(['reviews','currentUser', 'isLoggedIn']),
    hotReviews(){
      return _.sortBy(this.reviews, "like_users_count").reverse()
    },

  },
  methods:{
    ...mapActions(['fetchReviews']),
  },
  created(){
    this.fetchReviews()
  }
}
</script>

<style>
.table{
  text-decoration: none;
}
th {
  color: white;
}
td {
  color: white;
}
span {
  color: white;
}
.active{
  color: blue;
}
</style>