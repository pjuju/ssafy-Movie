<template>
  <div>
    <hr>
    <p class="text-start">댓글쓰기</p>
    <b-form @submit.prevent="onSubmit" class="d-flex justify-content-between pb-4" style="width:100%">
      <b-form-group
      label-for="input-1"
      style="width:93%"
      >
        <b-form-input id="input-1" v-model="content" required>
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">등록</b-button>
    </b-form>
      

  </div>

</template>

<script>
import { mapActions } from 'vuex'
export default {
  name:'CommentForm',
  data(){
    return {
      content: '',
    }
  },
  methods:{
    ...mapActions(['createComment']),
    onSubmit(){
      const payload ={
        moviePk: this.$route.params.moviePk,
        reviewPk: this.$route.params.reviewPk,
        content: this.content
      }
      this.createComment(payload)
      this.content = ''
    }
    
  },


}
</script>

<style>

</style>