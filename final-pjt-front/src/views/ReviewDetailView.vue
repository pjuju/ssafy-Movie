<template>
  <div v-if="isLoggedIn">
    <h1>Review</h1>
      <router-link :to="{ name: 'movie', params:{ moviePk: pk.moviePk } }">
        <h4 v-for="movie in review" :key="movie.id">
          {{movie.title}}
        </h4>
      </router-link>
    <div>
      제목:{{review.title}}
    </div>
    <div>
      내용:{{review.content}}
    </div>
    <div>
      시간:{{review.created_at}}
    </div>
    {{isAuthor}}
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
    댓글: {{review.comments_count}}개
    <comment-list :comments="review.comments"></comment-list>
    <!-- <div v-for="comment in review.comments" :key="comment.id">
      {{comment.content}}
    </div> -->
    <div>
      <comment-form></comment-form>
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
  methods:{
    ...mapActions(['fetchReview', 'deleteReview']),
  },
  computed:{
    ...mapGetters(['review', 'isAuthor','isLoggedIn'])
  },
  data(){
    return{
      pk:{ moviePk : this.$route.params.moviePk,
          reviewPk : this.$route.params.reviewPk
          },
    }
  },
  created(){
    this.fetchReview(this.pk)
  }
}
</script>

<style>

</style>