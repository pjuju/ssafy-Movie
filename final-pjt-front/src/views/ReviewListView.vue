<template>
  <div>
    <h1>ReviewList</h1>
    <div>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">영화</th>
            <th scope="col">제목</th>
            <th scope="col">작성자</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="review in reviews" :key="review.id">
            <th scope="row">{{review.id}}</th>
            <td>
              <router-link class="text-decoration-none"
               :to="{ name: 'movie', params: {moviePk: review.movie.id} }">
              <span>{{review.movie.title}}</span>
               </router-link>
              </td>
            <td>
              <router-link class="text-decoration-none"
              :to="{ name: 'reviewDetail', params: { moviePk: review.movie.id, reviewPk: review.id } }">
                <span>{{review.title}}</span>
              </router-link>
            </td>
            <td>
              {{review.user.username}}
            </td>
          </tr>

        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'ReviewListView',
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