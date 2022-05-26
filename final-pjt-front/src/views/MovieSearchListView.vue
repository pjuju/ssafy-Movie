<template>
  <div>
    {{title}}
    {{searchMovieList}}
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name:'MovieSearchListView',
  data(){
    return{
      title: this.$route.params.title,     
    }
  },
  computed:{
    ...mapGetters(['searchMovieList',]),

  },
  methods:{
    ...mapActions(['fetchSearchList',]),
  },

  created(){
    this.fetchSearchList(this.title)
  },
  
}
</script>

<style>

</style>