import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'


Vue.use(BootstrapVue)
Vue.use(VueGlide)
Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
