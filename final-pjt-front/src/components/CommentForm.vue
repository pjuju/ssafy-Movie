<template>
  <div>
    <form @submit.prevent="onSubmit">
      <label for="comment">댓글쓰기:</label>
      <input type="text" id="comment" v-model="content" required>
      <button>등록</button>
    </form>
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