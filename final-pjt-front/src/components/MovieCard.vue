<template>
  <div class= "movie-poster">
      <router-link :to=" { name: 'movie', params: { moviePk: movie.id } }">
        <img :src="imgUrl" class="m-1 rounded-3 shadow-sm" style="height: 300px; width: 200px; " alt="img">
      </router-link>     
          <p>{{movie.title}}</p>
  </div>
</template>

<script>
export default {
  name:'PopularMovie',
  props:{
    movie:Object,
  },
  data: function(){
  return {
    imgUrl:`https://image.tmdb.org/t/p/w500${this.movie.poster_path}`,
    }
  },

}
</script>

<style>
.movie-poster:hover{
  transform: scale(1.2);
  transition: 300ms ease-in-out;   
}
</style>