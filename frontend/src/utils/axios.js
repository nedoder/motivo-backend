import Vue from 'vue';

window.axios = require('axios');
// eslint-disable-next-line no-undef
axios.defaults.headers.common = {
  'X-Requested-With': 'XMLHttpRequest',
  Accept: 'application/json',
};
Vue.prototype.$http = window.axios;
