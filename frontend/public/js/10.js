(window["webpackJsonp"] = window["webpackJsonp"] || []).push([[10],{

/***/ "./node_modules/cache-loader/dist/cjs.js?!./node_modules/babel-loader/lib/index.js!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/CustomLogIn.vue?vue&type=script&lang=js&":
/*!*********************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/pages/CustomLogIn.vue?vue&type=script&lang=js& ***!
  \*********************************************************************************************************************************************************************************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! axios */ \"./node_modules/axios/index.js\");\n/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var _utils_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/utils/http */ \"./src/utils/http.js\");\n/* harmony import */ var _mixins_forms__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @/mixins/forms */ \"./src/mixins/forms.js\");\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n\naxios__WEBPACK_IMPORTED_MODULE_0___default.a.defaults.headers.get[\"Content-Type\"] = \"application/x-www-form-urlencoded\";\naxios__WEBPACK_IMPORTED_MODULE_0___default.a.defaults.headers.post[\"Content-Type\"] = \"multipart/form-data\";\n\n\n/* harmony default export */ __webpack_exports__[\"default\"] = ({\n  name: \"CustomLogIn\",\n  data: function data() {\n    return {\n      loginInfo: {\n        email: \"\",\n        password: \"\",\n        token: localStorage.getItem(\"user-token\") || null\n      }\n    };\n  },\n  mixins: [_mixins_forms__WEBPACK_IMPORTED_MODULE_2__[\"default\"]],\n  // @todo please use one empty line to separate elements like data, mixins, methods, mounted...\n  methods: {\n    // @todo my version\n    login: function login() {\n      var data = {\n        username: this.loginInfo.email,\n        password: this.loginInfo.password\n      };\n    },\n\n    /**\n     * Send email and password to authenticate user.\n     * Returns access and refresh token.\n     */\n    loginCustom: function loginCustom() {\n      var _this = this;\n\n      var data = {\n        email: this.loginInfo.email,\n        password: this.loginInfo.password\n      };\n      axios__WEBPACK_IMPORTED_MODULE_0___default()({\n        method: \"post\",\n        url: \"https://api.motivo.localhost/api/token/\",\n        data: data\n      }).then(function (resp) {\n        _this.token = resp.data.access;\n        localStorage.setItem(\"user-token\", resp.data.access);\n        localStorage.setItem(\"user-refresh\", resp.data.refresh);\n        var token = localStorage.getItem(\"user-token\");\n        var bearer = \"Bearer \" + token;\n        axios__WEBPACK_IMPORTED_MODULE_0___default()({\n          method: \"get\",\n          url: \"https://api.motivo.localhost/userdata/\",\n          headers: {\n            Authorization: bearer\n          }\n        }).then(function (resp) {\n          localStorage.setItem('user-id', resp.data.id);\n        }).catch(function (err) {\n          console.log(err);\n        }).finally(function () {\n          _this.$router.push(\"/dashboard/challenges/\");\n        });\n      }).catch(function (error) {\n        return console.log(error);\n      });\n    }\n  },\n  mounted: function mounted() {\n    var _this2 = this;\n\n    window.addEventListener(\"keyup\", function (event) {\n      if (event.keyCode === 13) {\n        console.log(\"Captured: \", event.key);\n\n        _this2.loginCustom();\n      }\n    });\n  }\n});\n\n//# sourceURL=webpack:///./src/views/pages/CustomLogIn.vue?./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "./node_modules/cache-loader/dist/cjs.js?{\"cacheDirectory\":\"node_modules/.cache/vue-loader\",\"cacheIdentifier\":\"1d97a420-vue-loader-template\"}!./node_modules/vue-loader/lib/loaders/templateLoader.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/CustomLogIn.vue?vue&type=template&id=6c6390fa&scoped=true&":
/*!*****************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/cache-loader/dist/cjs.js?{"cacheDirectory":"node_modules/.cache/vue-loader","cacheIdentifier":"1d97a420-vue-loader-template"}!./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/pages/CustomLogIn.vue?vue&type=template&id=6c6390fa&scoped=true& ***!
  \*****************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/*! exports provided: render, staticRenderFns */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"render\", function() { return render; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"staticRenderFns\", function() { return staticRenderFns; });\nvar render = function() {\n  var _vm = this\n  var _h = _vm.$createElement\n  var _c = _vm._self._c || _h\n  return _c(\"div\", { staticClass: \"wrapper-in\" }, [\n    _c(\"div\", { staticClass: \"motivo\" }, [\n      _c(\"img\", { attrs: { src: __webpack_require__(/*! ./img/motivo.png */ \"./src/views/pages/img/motivo.png\") } }),\n      _c(\"div\", { staticClass: \"formcontainer\" }, [\n        _c(\"form\", [\n          _vm._m(0),\n          _c(\"div\", { staticClass: \"form-group\" }, [\n            _c(\"label\", { attrs: { for: \"exampleFormControlInput1\" } }, [\n              _vm._v(\"Email\")\n            ]),\n            _c(\"input\", {\n              directives: [\n                {\n                  name: \"model\",\n                  rawName: \"v-model\",\n                  value: _vm.loginInfo.email,\n                  expression: \"loginInfo.email\"\n                }\n              ],\n              staticClass: \"form-control\",\n              attrs: {\n                type: \"email\",\n                id: \"exampleFormControlInput1\",\n                placeholder: \"Email\"\n              },\n              domProps: { value: _vm.loginInfo.email },\n              on: {\n                input: function($event) {\n                  if ($event.target.composing) {\n                    return\n                  }\n                  _vm.$set(_vm.loginInfo, \"email\", $event.target.value)\n                }\n              }\n            })\n          ]),\n          _c(\"div\", { staticClass: \"form-group\" }, [\n            _c(\"label\", { attrs: { for: \"exampleFormControlInput2\" } }, [\n              _vm._v(\"Password\")\n            ]),\n            _c(\"input\", {\n              directives: [\n                {\n                  name: \"model\",\n                  rawName: \"v-model\",\n                  value: _vm.loginInfo.password,\n                  expression: \"loginInfo.password\"\n                }\n              ],\n              staticClass: \"form-control\",\n              attrs: {\n                type: \"password\",\n                id: \"exampleFormControlInput2\",\n                placeholder: \"Password\"\n              },\n              domProps: { value: _vm.loginInfo.password },\n              on: {\n                input: function($event) {\n                  if ($event.target.composing) {\n                    return\n                  }\n                  _vm.$set(_vm.loginInfo, \"password\", $event.target.value)\n                }\n              }\n            })\n          ]),\n          _vm._m(1),\n          _c(\"div\", { staticClass: \"form-group\" }, [\n            _c(\n              \"button\",\n              {\n                staticClass: \"btn btn-info btn-lg btn-block\",\n                attrs: { type: \"button\" },\n                on: {\n                  click: function($event) {\n                    $event.preventDefault()\n                    return _vm.loginCustom.apply(null, arguments)\n                  }\n                }\n              },\n              [_vm._v(\" Login \")]\n            )\n          ]),\n          _vm._m(2)\n        ])\n      ])\n    ])\n  ])\n}\nvar staticRenderFns = [\n  function() {\n    var _vm = this\n    var _h = _vm.$createElement\n    var _c = _vm._self._c || _h\n    return _c(\"div\", [_c(\"h4\", [_vm._v(\"Sign in\")])])\n  },\n  function() {\n    var _vm = this\n    var _h = _vm.$createElement\n    var _c = _vm._self._c || _h\n    return _c(\"div\", { staticClass: \"form-group\" }, [\n      _c(\"a\", { attrs: { href: \"#\" } }, [_vm._v(\"Forgot password\")])\n    ])\n  },\n  function() {\n    var _vm = this\n    var _h = _vm.$createElement\n    var _c = _vm._self._c || _h\n    return _c(\"div\", { staticClass: \"form-group\" }, [\n      _c(\n        \"button\",\n        {\n          staticClass: \"btn btn-link btn-lg btn-block\",\n          attrs: { type: \"button\" }\n        },\n        [_vm._v(\" I don't have an account \")]\n      )\n    ])\n  }\n]\nrender._withStripped = true\n\n\n\n//# sourceURL=webpack:///./src/views/pages/CustomLogIn.vue?./node_modules/cache-loader/dist/cjs.js?%7B%22cacheDirectory%22:%22node_modules/.cache/vue-loader%22,%22cacheIdentifier%22:%221d97a420-vue-loader-template%22%7D!./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js?!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css&":
/*!***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src??ref--6-oneOf-1-2!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/pages/CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css& ***!
  \***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("// Imports\nvar ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../../../node_modules/css-loader/dist/runtime/api.js */ \"./node_modules/css-loader/dist/runtime/api.js\");\nexports = ___CSS_LOADER_API_IMPORT___(false);\n// Module\nexports.push([module.i, \"\\n.wrapper-in[data-v-6c6390fa] {\\n  background: #ffffff;\\n  height: 100vh;\\n}\\nform[data-v-6c6390fa] {\\n  width: 100%;\\n}\\n.formcontainer[data-v-6c6390fa] {\\n  width: 40%;\\n  margin: auto;\\n  margin-top: 10%;\\n}\\n.motivo[data-v-6c6390fa] {\\n  width: 100%;\\n  margin: auto;\\n  padding: 30px 50px;\\n}\\nh4[data-v-6c6390fa] {\\n  text-align: center;\\n  padding-bottom: 1rem;\\n  font-size: 24px;\\n  color: #6d7885;\\n}\\na[data-v-6c6390fa],\\n.btn-link[data-v-6c6390fa] {\\n  color: #1cb0f6;\\n  font-weight: bold;\\n  font-size: 18px;\\n}\\nlabel[data-v-6c6390fa] {\\n  color: #99a2ad;\\n  font-size: 14px;\\n}\\n.btn-link[data-v-6c6390fa] {\\n  -webkit-box-shadow: 1px 1px 3px #99a2ad;\\n          box-shadow: 1px 1px 3px #99a2ad;\\n  text-decoration: none;\\n}\\n.btn-info[data-v-6c6390fa] {\\n  font-weight: bold;\\n}\\ninput[data-v-6c6390fa],\\nbutton[data-v-6c6390fa] {\\n  border-radius: 12px;\\n  padding: 10px;\\n}\\ninput[data-v-6c6390fa] {\\n  font-size: 18px;\\n  background: #f7f8fa;\\n}\\n\", \"\"]);\n// Exports\nmodule.exports = exports;\n\n\n//# sourceURL=webpack:///./src/views/pages/CustomLogIn.vue?./node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src??ref--6-oneOf-1-2!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "./node_modules/vue-style-loader/index.js?!./node_modules/css-loader/dist/cjs.js?!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css&":
/*!*****************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/vue-style-loader??ref--6-oneOf-1-0!./node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src??ref--6-oneOf-1-2!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/pages/CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css& ***!
  \*****************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("// style-loader: Adds some css to the DOM by adding a <style> tag\n\n// load the styles\nvar content = __webpack_require__(/*! !../../../node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!../../../node_modules/vue-loader/lib/loaders/stylePostLoader.js!../../../node_modules/postcss-loader/src??ref--6-oneOf-1-2!../../../node_modules/cache-loader/dist/cjs.js??ref--0-0!../../../node_modules/vue-loader/lib??vue-loader-options!./CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css& */ \"./node_modules/css-loader/dist/cjs.js?!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css&\");\nif(content.__esModule) content = content.default;\nif(typeof content === 'string') content = [[module.i, content, '']];\nif(content.locals) module.exports = content.locals;\n// add the styles to the DOM\nvar add = __webpack_require__(/*! ../../../node_modules/vue-style-loader/lib/addStylesClient.js */ \"./node_modules/vue-style-loader/lib/addStylesClient.js\").default\nvar update = add(\"7f4a09a8\", content, false, {\"sourceMap\":false,\"shadowMode\":false});\n// Hot Module Replacement\nif(false) {}\n\n//# sourceURL=webpack:///./src/views/pages/CustomLogIn.vue?./node_modules/vue-style-loader??ref--6-oneOf-1-0!./node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src??ref--6-oneOf-1-2!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "./src/utils/http.js":
/*!***************************!*\
  !*** ./src/utils/http.js ***!
  \***************************/
/*! exports provided: esc, qs, postRequest, postMultipartRequest, putRequest, patchRequest, deleteRequest, getRequest, downloadRequest, uploadRequest, default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"esc\", function() { return esc; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"qs\", function() { return qs; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"postRequest\", function() { return postRequest; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"postMultipartRequest\", function() { return postMultipartRequest; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"putRequest\", function() { return putRequest; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"patchRequest\", function() { return patchRequest; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"deleteRequest\", function() { return deleteRequest; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"getRequest\", function() { return getRequest; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"downloadRequest\", function() { return downloadRequest; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"uploadRequest\", function() { return uploadRequest; });\n/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! axios */ \"./node_modules/axios/index.js\");\n/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_0__);\nfunction _typeof(obj) { \"@babel/helpers - typeof\"; if (typeof Symbol === \"function\" && typeof Symbol.iterator === \"symbol\") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === \"function\" && obj.constructor === Symbol && obj !== Symbol.prototype ? \"symbol\" : typeof obj; }; } return _typeof(obj); }\n\n/* eslint-disable no-undef */\n\nvar api = axios__WEBPACK_IMPORTED_MODULE_0___default.a.create({\n  withCredentials: true,\n  baseURL: Object({\"NODE_ENV\":\"development\",\"BASE_URL\":\"/\"}).VUE_APP_API_URL,\n  timeout: 50000,\n  headers: {\n    'X-Requested-With': 'XMLHttpRequest',\n    Accept: 'application/json'\n  }\n});\napi.interceptors.response.use(function (response) {\n  // Any status code that lie within the range of 2xx cause this function to trigger\n  // Do something with response data\n  if (response.data.message) {// vm.$notifySuccess(response.data.message);\n  }\n\n  return response;\n}, function (error) {\n  if (_typeof(error) !== 'object' || !('response' in error)) {\n    return;\n  }\n\n  if (error.response) {\n    if (error.response.status === 429) {\n      vm.$notifyError('Too Many Attempts.'); // wyskakujace powiadomienia z coreUI\n    }\n\n    if (error.response.status === 403) {\n      console.error(\"403: \".concat(error.request.responseURL));\n      vm.$notifyError('You don\\'t have right to this resource!');\n    }\n\n    if (error.response.status === 401) {\n      // Unauthorized error\n      console.error(\"401: \".concat(error.request.responseURL));\n      window.sessionStorage.setItem('intended', vm.$router.currentRoute.fullPath);\n      vm.$router.push({\n        name: 'auth.login'\n      });\n    } // CSRF Token error, repeat last request\n\n\n    if (error.response.status === 419) {\n      // eslint-disable-next-line consistent-return\n      return api.get('/sanctum/csrf-cookie').then(function () {\n        return axios__WEBPACK_IMPORTED_MODULE_0___default()(error.response.config);\n      }).catch(function (tokenError) {\n        console.error({\n          tokenError: tokenError\n        });\n        return Promise.reject(tokenError);\n      });\n    } // this fragment should be last\n    // if (error.response.status !== 422) {\n    //   const msg = error.response.data.message || error.message;\n    //   this.$message.error(msg);\n    // }\n\n  } else if (error.request) {\n    console.log({\n      'Request error': error.request\n    });\n  } else {\n    console.log('Error', error.message);\n  }\n\n  console.log('rejected'); // eslint-disable-next-line consistent-return\n\n  return Promise.reject(error);\n});\nvar esc = encodeURIComponent;\nfunction qs(params) {\n  return Object.keys(params).map(function (k) {\n    return \"\".concat(esc(k), \"=\").concat(esc(params[k]));\n  }).join('&');\n}\nfunction postRequest(uri) {\n  var data = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};\n  return new Promise(function (resolve, reject) {\n    api.post(uri, data).then(function (response) {\n      resolve(response.data);\n    }).catch(function (errors) {\n      console.log({\n        errors: errors\n      });\n      reject(errors.response);\n    });\n  });\n}\nfunction postMultipartRequest(uri, formData) {\n  return new Promise(function (resolve, reject) {\n    api.post(uri, formData).then(function (response) {\n      // checkResponse(response)\n      resolve(response.data);\n    }).catch(function (errors) {\n      // checkError(errors)\n      if ('response' in errors) {\n        reject(errors.response);\n      }\n\n      if ('error' in errors) {\n        reject(errors.error);\n      }\n    });\n  });\n}\nfunction putRequest(uri) {\n  var data = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};\n  return new Promise(function (resolve, reject) {\n    api.put(uri, data).then(function (response) {\n      resolve(response.data);\n    }).catch(function (errors) {\n      reject(errors.response);\n    });\n  });\n}\nfunction patchRequest(uri) {\n  var data = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};\n  return new Promise(function (resolve, reject) {\n    api.patch(uri, data).then(function (response) {\n      resolve(response.data);\n    }).catch(function (errors) {\n      reject(errors.response);\n    });\n  });\n}\nfunction deleteRequest(uri) {\n  var data = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};\n  return new Promise(function (resolve, reject) {\n    api.delete(uri, data).then(function (response) {\n      resolve(response.data);\n    }).catch(function (errors) {\n      reject(errors.response);\n    });\n  });\n}\nfunction getRequest(url) {\n  var data = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};\n  var uri = url;\n\n  if (Object.keys(data).length > 0) {\n    uri = \"\".concat(uri, \"?\").concat(qs(data));\n  }\n\n  return new Promise(function (resolve, reject) {\n    api.get(uri).then(function (response) {\n      resolve(response.data);\n    }).catch(function (errors) {\n      reject(errors.response);\n    });\n  });\n}\nfunction downloadRequest(url, filename) {\n  var data = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : {};\n  var uri = url;\n\n  if (Object.keys(data).length > 0) {\n    uri = \"\".concat(uri, \"?\").concat(qs(data));\n  }\n\n  return new Promise(function (resolve, reject) {\n    api.get(uri, {\n      responseType: 'blob',\n      headers: {}\n    }).then(function (response) {\n      var link = document.createElement('a');\n      link.href = window.URL.createObjectURL(new Blob([response.data]));\n      link.setAttribute('download', filename);\n      document.body.appendChild(link);\n      link.click();\n    }).catch(function (errors) {\n      reject(errors.response);\n    });\n  });\n}\nfunction uploadRequest(uri, data) {\n  return fetch(uri, {\n    headers: {},\n    cors: true,\n    method: 'POST',\n    body: data\n  });\n}\n/* harmony default export */ __webpack_exports__[\"default\"] = (api);\n\n//# sourceURL=webpack:///./src/utils/http.js?");

/***/ }),

/***/ "./src/views/pages/CustomLogIn.vue":
/*!*****************************************!*\
  !*** ./src/views/pages/CustomLogIn.vue ***!
  \*****************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _CustomLogIn_vue_vue_type_template_id_6c6390fa_scoped_true___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./CustomLogIn.vue?vue&type=template&id=6c6390fa&scoped=true& */ \"./src/views/pages/CustomLogIn.vue?vue&type=template&id=6c6390fa&scoped=true&\");\n/* harmony import */ var _CustomLogIn_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./CustomLogIn.vue?vue&type=script&lang=js& */ \"./src/views/pages/CustomLogIn.vue?vue&type=script&lang=js&\");\n/* empty/unused harmony star reexport *//* harmony import */ var _CustomLogIn_vue_vue_type_style_index_0_id_6c6390fa_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css& */ \"./src/views/pages/CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css&\");\n/* harmony import */ var _node_modules_vue_loader_lib_runtime_componentNormalizer_js__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../../node_modules/vue-loader/lib/runtime/componentNormalizer.js */ \"./node_modules/vue-loader/lib/runtime/componentNormalizer.js\");\n\n\n\n\n\n\n/* normalize component */\n\nvar component = Object(_node_modules_vue_loader_lib_runtime_componentNormalizer_js__WEBPACK_IMPORTED_MODULE_3__[\"default\"])(\n  _CustomLogIn_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_1__[\"default\"],\n  _CustomLogIn_vue_vue_type_template_id_6c6390fa_scoped_true___WEBPACK_IMPORTED_MODULE_0__[\"render\"],\n  _CustomLogIn_vue_vue_type_template_id_6c6390fa_scoped_true___WEBPACK_IMPORTED_MODULE_0__[\"staticRenderFns\"],\n  false,\n  null,\n  \"6c6390fa\",\n  null\n  \n)\n\n/* hot reload */\nif (false) { var api; }\ncomponent.options.__file = \"src/views/pages/CustomLogIn.vue\"\n/* harmony default export */ __webpack_exports__[\"default\"] = (component.exports);\n\n//# sourceURL=webpack:///./src/views/pages/CustomLogIn.vue?");

/***/ }),

/***/ "./src/views/pages/CustomLogIn.vue?vue&type=script&lang=js&":
/*!******************************************************************!*\
  !*** ./src/views/pages/CustomLogIn.vue?vue&type=script&lang=js& ***!
  \******************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _node_modules_cache_loader_dist_cjs_js_ref_12_0_node_modules_babel_loader_lib_index_js_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_CustomLogIn_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../node_modules/cache-loader/dist/cjs.js??ref--12-0!../../../node_modules/babel-loader/lib!../../../node_modules/cache-loader/dist/cjs.js??ref--0-0!../../../node_modules/vue-loader/lib??vue-loader-options!./CustomLogIn.vue?vue&type=script&lang=js& */ \"./node_modules/cache-loader/dist/cjs.js?!./node_modules/babel-loader/lib/index.js!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/CustomLogIn.vue?vue&type=script&lang=js&\");\n/* empty/unused harmony star reexport */ /* harmony default export */ __webpack_exports__[\"default\"] = (_node_modules_cache_loader_dist_cjs_js_ref_12_0_node_modules_babel_loader_lib_index_js_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_CustomLogIn_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_0__[\"default\"]); \n\n//# sourceURL=webpack:///./src/views/pages/CustomLogIn.vue?");

/***/ }),

/***/ "./src/views/pages/CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css&":
/*!**************************************************************************************************!*\
  !*** ./src/views/pages/CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css& ***!
  \**************************************************************************************************/
/*! no static exports found */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _node_modules_vue_style_loader_index_js_ref_6_oneOf_1_0_node_modules_css_loader_dist_cjs_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_CustomLogIn_vue_vue_type_style_index_0_id_6c6390fa_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../node_modules/vue-style-loader??ref--6-oneOf-1-0!../../../node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!../../../node_modules/vue-loader/lib/loaders/stylePostLoader.js!../../../node_modules/postcss-loader/src??ref--6-oneOf-1-2!../../../node_modules/cache-loader/dist/cjs.js??ref--0-0!../../../node_modules/vue-loader/lib??vue-loader-options!./CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css& */ \"./node_modules/vue-style-loader/index.js?!./node_modules/css-loader/dist/cjs.js?!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/CustomLogIn.vue?vue&type=style&index=0&id=6c6390fa&scoped=true&lang=css&\");\n/* harmony import */ var _node_modules_vue_style_loader_index_js_ref_6_oneOf_1_0_node_modules_css_loader_dist_cjs_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_CustomLogIn_vue_vue_type_style_index_0_id_6c6390fa_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_vue_style_loader_index_js_ref_6_oneOf_1_0_node_modules_css_loader_dist_cjs_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_CustomLogIn_vue_vue_type_style_index_0_id_6c6390fa_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__);\n/* harmony reexport (unknown) */ for(var __WEBPACK_IMPORT_KEY__ in _node_modules_vue_style_loader_index_js_ref_6_oneOf_1_0_node_modules_css_loader_dist_cjs_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_CustomLogIn_vue_vue_type_style_index_0_id_6c6390fa_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__) if([\"default\"].indexOf(__WEBPACK_IMPORT_KEY__) < 0) (function(key) { __webpack_require__.d(__webpack_exports__, key, function() { return _node_modules_vue_style_loader_index_js_ref_6_oneOf_1_0_node_modules_css_loader_dist_cjs_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_CustomLogIn_vue_vue_type_style_index_0_id_6c6390fa_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__[key]; }) }(__WEBPACK_IMPORT_KEY__));\n\n\n//# sourceURL=webpack:///./src/views/pages/CustomLogIn.vue?");

/***/ }),

/***/ "./src/views/pages/CustomLogIn.vue?vue&type=template&id=6c6390fa&scoped=true&":
/*!************************************************************************************!*\
  !*** ./src/views/pages/CustomLogIn.vue?vue&type=template&id=6c6390fa&scoped=true& ***!
  \************************************************************************************/
/*! exports provided: render, staticRenderFns */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _node_modules_cache_loader_dist_cjs_js_cacheDirectory_node_modules_cache_vue_loader_cacheIdentifier_1d97a420_vue_loader_template_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_CustomLogIn_vue_vue_type_template_id_6c6390fa_scoped_true___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../node_modules/cache-loader/dist/cjs.js?{\"cacheDirectory\":\"node_modules/.cache/vue-loader\",\"cacheIdentifier\":\"1d97a420-vue-loader-template\"}!../../../node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!../../../node_modules/cache-loader/dist/cjs.js??ref--0-0!../../../node_modules/vue-loader/lib??vue-loader-options!./CustomLogIn.vue?vue&type=template&id=6c6390fa&scoped=true& */ \"./node_modules/cache-loader/dist/cjs.js?{\\\"cacheDirectory\\\":\\\"node_modules/.cache/vue-loader\\\",\\\"cacheIdentifier\\\":\\\"1d97a420-vue-loader-template\\\"}!./node_modules/vue-loader/lib/loaders/templateLoader.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/CustomLogIn.vue?vue&type=template&id=6c6390fa&scoped=true&\");\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"render\", function() { return _node_modules_cache_loader_dist_cjs_js_cacheDirectory_node_modules_cache_vue_loader_cacheIdentifier_1d97a420_vue_loader_template_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_CustomLogIn_vue_vue_type_template_id_6c6390fa_scoped_true___WEBPACK_IMPORTED_MODULE_0__[\"render\"]; });\n\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"staticRenderFns\", function() { return _node_modules_cache_loader_dist_cjs_js_cacheDirectory_node_modules_cache_vue_loader_cacheIdentifier_1d97a420_vue_loader_template_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_CustomLogIn_vue_vue_type_template_id_6c6390fa_scoped_true___WEBPACK_IMPORTED_MODULE_0__[\"staticRenderFns\"]; });\n\n\n\n//# sourceURL=webpack:///./src/views/pages/CustomLogIn.vue?");

/***/ }),

/***/ "./src/views/pages/img/motivo.png":
/*!****************************************!*\
  !*** ./src/views/pages/img/motivo.png ***!
  \****************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("module.exports = __webpack_require__.p + \"img/motivo.8d8c7d58.png\";\n\n//# sourceURL=webpack:///./src/views/pages/img/motivo.png?");

/***/ })

}]);