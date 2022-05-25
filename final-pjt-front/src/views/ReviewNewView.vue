<template>
  <div>
    <review-form :review="review" action="create"></review-form>
  </div>
</template>

<script>
import ReviewForm from "@/components/ReviewForm"
export default {
  name:"ReviewNewView",
  components:{
    ReviewForm
  },
  data(){
    return{
      review:{
        title: '',
        content: '',
        rank: null,
      }
    }
  }
}
</script>

<style>

</style>