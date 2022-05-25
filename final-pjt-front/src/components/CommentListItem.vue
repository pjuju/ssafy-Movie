<template>
  <div @mouseover="upHere = true" @mouseleave="upHere = false">
    <span v-if="!isEditing">
      {{comment.content}}
    </span>
    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate">등록</button>
      <button @click="switchIsEditing">취소</button>      
    </span>
    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button v-show="upHere" @click="switchIsEditing">수정</button>
      <button v-show="upHere" @click="deleteComment(payload)">삭제</button>
    </span>
  </div>
</template>

<script>
import { mapActions, mapGetters} from 'vuex'
export default {
  name:'commentListItem',
  props:{
    comment:Object,
  },
  data(){
    return{
      isEditing: false,
      payload:{
        moviePk: this.$route.params.moviePk,
        reviewPk: this.$route.params.reviewPk,
        commentPk: this.comment.id,
        content: this.comment.content,
      },
      upHere: false,
    }
  },
  computed:{
    ...mapGetters(['currentUser'])
  },
  methods:{
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing(){
      this.isEditing = !this.isEditing
    },
    onUpdate(){
      this.updateComment(this.payload)
      this.isEditing = false
    }
    
  },

}
</script>

<style>

</style>