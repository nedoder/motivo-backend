import 'core-js/stable'
import Vue from 'vue'
import App from './App'
import router from './router'
import CoreuiVue from '@coreui/vue'
import { iconsSet as icons } from './assets/icons/icons.js'
import store from './store'
import './plugins'
import linkify from 'vue-linkify'

Vue.config.performance = true
Vue.use(CoreuiVue)
Vue.prototype.$log = console.log.bind(console)
Vue.directive('linkified', linkify)

new Vue({
    el: '#app',
    router,
    store,
    icons,
    template: '<App/>',
    components: {
        App
    }
})