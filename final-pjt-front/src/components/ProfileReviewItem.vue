<template>
  <div>
    <div class="col">
    <div class="card">
       <router-link class="text-decoration-none text-white" style="background-color:rgba( 48, 47, 48)"
        :to="{ name: 'reviewDetail', params: { moviePk: review.movie, reviewPk: review.id } }">

      <div class="pt-1 card-body pb-0">
          <p>{{review.movie.title}}</p>
            <p class="fw-bold">{{review.title | cutTitle }}</p>      
          <div>
          <i v-for="i in review.rank" :key="i" style="color:orange;" class="fa-solid fa-star mb-3"></i>
          </div>

      </div>
        <p class="text-muted pb-0">{{review.user.username}}</p>       


      </router-link>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name:'ProfileReviewItem',
  props:{
    review:Object,
  }
}
</script>

<style>

</style>