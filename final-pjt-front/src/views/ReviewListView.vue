<template>
  <div>
    <h1>ReviewList</h1>

  <div class="row row-cols-2 row-cols-md-4 row-cols-xl-6">
      <review-list-item class="mb-4" v-for="review in reviews" :key="review.id" :review="review"></review-list-item>
  </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import ReviewListItem from '@/components/ReviewListItem.vue'

export default {
  name:'ReviewListView',
  components:{ ReviewListItem },
  computed:{
    ...mapGetters(['reviews'])
  },
  methods:{
    ...mapActions(['fetchReviews'])
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
</style>