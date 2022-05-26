<template>
  <div>
    <comment-list-item
      v-for="comment in comments" :key="comment.id" :comment="comment">

    </comment-list-item>
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