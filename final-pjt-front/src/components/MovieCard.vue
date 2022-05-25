<template>
  <div>       
      <router-link :to=" { name: 'movie', params: { moviePk: movie.id } }">
        <img :src="imgUrl" class="card-img-top m-1" style="height: 300px; width: 200px;" alt="img">
      </router-link>     
          <p class="fw-bold">{{movie.title}}</p>
  </div>
</template>

<script>
export default {
  name:'PopularMovie',
  props:{
    movie:Object,
  },
  methods:{
    
  },
  data: function(){
  return {
    imgUrl:`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`,
    // id : this.movie.tmdb_id ? this.movie.tmdb_id : this.movie.id
    }
  },

}
</script>

<style>

</style>