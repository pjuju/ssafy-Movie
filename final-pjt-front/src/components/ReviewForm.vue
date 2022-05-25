<template>
  <div>
    <star-rating
     :rating="newReview.rank"
     :increment="1"
     class="d-flex justify-content-center"
     v-model="newReview.rank"
     ></star-rating>
    <b-form @submit.prevent="onSubmit" class="col-6">
        <p class="d-flex">제목:</p>
        <b-form-input
          id="input-1"
          v-model="newReview.title"
          placeholder="제목"
          required
        ></b-form-input>
      <br>
        <p class="d-flex">내용:</p>
        <b-form-textarea 
          id="input-2"
          v-model="newReview.content"
          placeholder="내용을 입력하세요"
          rows="12"
          required
        ></b-form-textarea>
      <b-button class="m-4" type="submit" variant="primary">작성하기</b-button>
    </b-form>

    <!-- <form @submit.prevent="onSubmit">
      <div>
        <label for="title">title: </label>
        <input v-model="newReview.title" type="text" id="title" />
      </div>
      <div>
        <label for="content">content: </label>
        <textarea v-model="newReview.content" type="text" id="content"></textarea>
      </div>
      <div>
        <label for="rank">rank:</label>
        <input type="text" id="rank" v-model="newReview.rank" />
      </div>
      <div>
        <button>{{ action }}</button>
      </div>
   </form> -->
  </div>
</template>

<script>
import {mapActions} from 'vuex'
import StarRating from 'vue-star-rating'

export default {
  name:'ReviewForm',
  components:{
    StarRating
  },
  props:{
    review:Object,
    action:String,
  },
  data(){
    return{
      newReview:{
      title: this.review.title,
      content: this.review.content,
      rank: this.review.rank,
      }
    }
  },
  methods:{
    ...mapActions(['createReview', 'updateReview']),
    onSubmit(){
      if (this.action == 'create'){
        const payload = {
          moviePk: this.$route.params.moviePk,
          ...this.newReview
        }
        this.createReview(payload)
      }
      else if (this.action == 'update'){
        const payload = {
          moviePk: this.$route.params.moviePk,
          reviewPk: this.$route.params.reviewPk,
          ...this.newReview
        }
        this.updateReview(payload)
      }
    }
  }

}
</script>

<style>
form { 
margin: 0 auto; 
width:250px;
}
</style>