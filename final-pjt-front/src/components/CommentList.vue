<template>
  <div>
    <h1>CommentList</h1>
    <comment-list-item
      v-for="comment in comments" :key="comment.id" :comment="comment">

    </comment-list-item>
    <!-- <div v-for="comment in comments" :key="comment.id">
      {{comment.content}}
      <span>
        <button>수정</button>
        <button>삭제</button>
      </span>
    </div> -->
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'

export default {
  name:'CommentList',
  components:{
    CommentListItem,
  },
  props:{
    comments:Array,
  },
  methods:{
  }

  }
</script>

<style>

</style>