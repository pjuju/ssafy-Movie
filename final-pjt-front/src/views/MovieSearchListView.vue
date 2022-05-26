<template>
  <div>
    
    <p class="d-flex justify-content-start ms-3 fs-4">{{title}} 검색 결과: {{searchMovieList.length}}개</p>
    
    <div v-if="searchMovieList">      
      <div v-if="searchMovieList.length > 8">
        <vue-glide 
          class="glide__track"
          data-glide-el="track"
          ref="slider"
          type="carousel"
          :breakpoints="{ 3000: {perView: 7}, 1500: {perView: 4}, 1000: {perView: 2} }"
          :gap="10">
            <vue-glide-slide v-for="movie in searchMovieList" :key="movie.id">
              <movie-card :movie="movie" />
          </vue-glide-slide>
        </vue-glide>
      </div>
      <div class="d-flex justify-content-start" v-if="searchMovieList.length <= 8">
        <div id="littlecount" v-for="movie in searchMovieList" :key="movie.id">
          <movie-card :movie="movie" />
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieCard from '@/components/MovieCard.vue'
import { Glide, GlideSlide } from 'vue-glide-js'


export default {
  name:'MovieSearchListView',
  components:{
    MovieCard,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide
  },
 
  computed:{
    ...mapGetters(['searchMovieList',]),
    title() {return this.$route.params.title}
  },
  methods:{
    ...mapActions(['fetchSearchList',]),
  },

  created(){
    this.fetchSearchList(this.$route.params.title)
  },
  
  
}
</script>

<style>

</style>