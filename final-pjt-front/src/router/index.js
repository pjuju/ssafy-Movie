import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'

import MovieListView from '@/views/MovieListView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue' 

import ReviewNewView from '@/views/ReviewNewView.vue'
import ReviewEditView from '@/views/ReviewEditView.vue'
import ReviewDetailView from '@/views/ReviewDetailView.vue'
import ReviewListView from '@/views/ReviewListView.vue'
import MovieSearchListView from '@/views/MovieSearchListView.vue'

import NotFound404 from '@/views/NotFound404.vue'




Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/', // home
    name: 'movies',
    component: MovieListView
  },
  {
    path: '/movies/:moviePk',
    name: 'movie',
    component: MovieDetailView
  },
  {
    path: '/movies/:moviePk/review/new',
    name: 'reviewNew',
    component: ReviewNewView
  },
  {
    path: '/movies/:moviePk/review/:reviewPk/edit/',
    name: 'reviewEdit',
    component: ReviewEditView
  },
  {
    path: '/movies/:moviePk/review/:reviewPk',
    name: 'reviewDetail',
    component: ReviewDetailView
  },
  {
    path: '/reviews',
    name: 'review',
    component: ReviewListView
  },
  {
    path: '/search/:title',
    name: 'movieSearchList',
    component: MovieSearchListView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
