<template>
  <div class="comment-box">
    <div class="user-box d-flex">
      <small><i class="fa-solid fa-user"></i></small>
      <p class="ms-1 pt-0"><small>
        <router-link class="text-decoration-none text-white" :to="{ name:'profile', params:{ username: comment.user.username} }">
          {{comment.user.username}}</router-link></small></p>
      <p class="text-muted text-end ms-2"><small> {{comment.updated_at | cutDate }}</small></p>
      <span v-if="currentUser.username === comment.user.username && !isEditing" class="ms-2">
      <i class="fa-solid fa-pen-to-square me-1" @click="switchIsEditing"></i>
      <i class="fa-solid fa-trash-can" @click="deleteComment(payload)"></i>
    </span>
    </div>

    <p v-if="!isEditing" class="text-start">
      {{comment.content}}
    </p>
    
    <span v-if="isEditing">
      <b-form style="width:80%">
        <b-form-group label-for="input-1" class="mb-2">
        <b-form-input id="input-1" v-model="payload.content"></b-form-input>
        </b-form-group>
      <b-button variant="primary" class="me-2" @click="onUpdate">수정</b-button>
      <b-button  @click="switchIsEditing">취소</b-button>      
      </b-form>
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
    }
  },
  computed:{
    ...mapGetters(['currentUser']),
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
  filters:{
    cutDate(value){
      return value.slice(0, 10)
    }
  }

}
</script>

<style>

</style>