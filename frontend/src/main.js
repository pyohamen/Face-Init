// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
import RouterPrefetch from 'vue-router-prefetch'
import App from './App'
import router from './router'

// validate 추가
import * as VeeValidate from 'vee-validate'

// vuex 추가
import store from './store'

// 실시간 시간 표현
import moment from 'moment'
import VueMomentJS from 'vue-moment'

// template 추가
import BlackDashboard from './plugins/blackDashboard'

// 현지 언어 설정
import i18n from './i18n'

// registerServiceWorker 추가
import './registerServiceWorker'

// bootstrap 추가
import BootstrapVue from 'bootstrap-vue'

Vue.use(BlackDashboard)
Vue.use(VueRouter)
Vue.use(RouterPrefetch)
Vue.use(VueMomentJS, moment)
Vue.use(BootstrapVue)
Vue.config.productionTip = false

Vue.use(VeeValidate)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  i18n,
  components: { App },
  template: '<App/>'
})
