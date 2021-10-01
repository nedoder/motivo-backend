(window["webpackJsonp"] = window["webpackJsonp"] || []).push([[13],{

/***/ "./node_modules/cache-loader/dist/cjs.js?!./node_modules/babel-loader/lib/index.js!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/Awards.vue?vue&type=script&lang=js&":
/*!****************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/pages/Awards.vue?vue&type=script&lang=js& ***!
  \****************************************************************************************************************************************************************************************************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! axios */ \"./node_modules/axios/index.js\");\n/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_0__);\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n//\n\n/* harmony default export */ __webpack_exports__[\"default\"] = ({\n  name: 'Awards',\n  data: function data() {\n    return {\n      awards: []\n    };\n  },\n  //   watch: {\n  //     $route: {\n  //       immediate: true,\n  //       handler (route) {\n  //         if (route.query && route.query.page) {\n  //           this.activePage = Number(route.query.page)\n  //         }\n  //       }\n  //     }\n  //   },\n  //   methods: {\n  //     getBadge (status) {\n  //       switch (status) {\n  //         case 'Active': return 'success'\n  //         case 'Inactive': return 'secondary'\n  //         case 'Pending': return 'warning'\n  //         case 'Banned': return 'danger'\n  //         default: 'primary'\n  //       }\n  //     },\n  //     rowClicked (item, index) {\n  //       this.$router.push({path: `users/${index + 1}`})\n  //     },\n  //     pageChange (val) {\n  //       this.$router.push({ query: { page: val }})\n  //     }\n  //   }\n  mounted: function mounted() {\n    var _this = this;\n\n    var token = localStorage.getItem('user-token');\n    var bearer = 'Bearer ' + token;\n    axios__WEBPACK_IMPORTED_MODULE_0___default()({\n      method: 'get',\n      url: 'https://api.motivo.localhost/awards/',\n      headers: {\n        'Authorization': bearer\n      }\n    }).then(function (resp) {\n      _this.awards = resp.data;\n\n      _this.awards.sort(function (a, b) {\n        return a.awards_left - b.awards_left;\n      }); // this.title = resp.data.results[0].title\n      // this.price = resp.data.results[0.].price\n      // this.image = resp.data.results[0].image\n\n\n      console.log(resp.data[0]);\n    }).catch(function (error) {\n      return console.log(error);\n    });\n  },\n  methods: {\n    couponClicked: function couponClicked(award) {\n      this.$router.push({\n        path: \"/dashboard/awards/\".concat(award.id)\n      });\n    }\n  }\n});\n\n//# sourceURL=webpack:///./src/views/pages/Awards.vue?./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "./node_modules/cache-loader/dist/cjs.js?{\"cacheDirectory\":\"node_modules/.cache/vue-loader\",\"cacheIdentifier\":\"1d97a420-vue-loader-template\"}!./node_modules/vue-loader/lib/loaders/templateLoader.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/Awards.vue?vue&type=template&id=0b2caf1b&":
/*!************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/cache-loader/dist/cjs.js?{"cacheDirectory":"node_modules/.cache/vue-loader","cacheIdentifier":"1d97a420-vue-loader-template"}!./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/pages/Awards.vue?vue&type=template&id=0b2caf1b& ***!
  \************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/*! exports provided: render, staticRenderFns */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"render\", function() { return render; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"staticRenderFns\", function() { return staticRenderFns; });\nvar render = function() {\n  var _vm = this\n  var _h = _vm.$createElement\n  var _c = _vm._self._c || _h\n  return _c(\"div\", [\n    _c(\n      \"div\",\n      { staticClass: \"wrapper\" },\n      [\n        _c(\n          \"CRow\",\n          { attrs: { fluid: \"\" } },\n          _vm._l(_vm.awards, function(award) {\n            return _c(\n              \"CCol\",\n              { style: { padding: \"1px\" }, attrs: { sm: \"4\" } },\n              [\n                _c(\n                  \"div\",\n                  { staticClass: \"award_card\" },\n                  [\n                    _c(\n                      \"CCard\",\n                      {\n                        staticClass: \"bg-secondary\",\n                        style: [\n                          award.awards_left === 0\n                            ? {\n                                background: \"rgba(153,162,173, 0.2)\",\n                                borderRadius: \"18px !important\"\n                              }\n                            : {\n                                background: \"transparent\",\n                                borderRadius: \"18px !important\"\n                              }\n                        ],\n                        on: {\n                          click: function($event) {\n                            award.awards_left === 0\n                              ? null\n                              : _vm.couponClicked(award)\n                          }\n                        }\n                      },\n                      [\n                        _c(\n                          \"CCardBody\",\n                          {\n                            staticClass: \"hover\",\n                            style: {\n                              color: \"#F2C94C\",\n                              padding: \"50px 10px 10px 10px\",\n                              fontWeight: \"bold\",\n                              height: \"250px\",\n                              margin: \"0px\",\n                              borderRadius: \"18px\",\n                              fontSize: \"24px\",\n                              background: \"transparent\"\n                            }\n                          },\n                          [\n                            _c(\n                              \"div\",\n                              { style: { color: \"#03001D\", margin: \"2px 0\" } },\n                              [\n                                _c(\"h2\", { style: { fontSize: \"1.5em\" } }, [\n                                  _vm._v(_vm._s(award.title))\n                                ])\n                              ]\n                            ),\n                            _c(\n                              \"div\",\n                              {\n                                style: {\n                                  color: \"#03001D\",\n                                  fontSize: \"16px\",\n                                  fontWeight: \"500\",\n                                  marginTop: \"20px\"\n                                }\n                              },\n                              [\n                                _c(\"h6\", { style: { color: \"#6D7885\" } }, [\n                                  _vm._v(\n                                    \" Awards left: \" +\n                                      _vm._s(award.awards_left) +\n                                      \" \"\n                                  )\n                                ])\n                              ]\n                            ),\n                            _c(\n                              \"div\",\n                              {\n                                style: {\n                                  color: \"#6D7885\",\n                                  fontSize: \"14px\",\n                                  fontWeight: \"400\",\n                                  marginTop: \"20px\"\n                                }\n                              },\n                              [\n                                _c(\"p\", [\n                                  _vm._v(\n                                    \" Description: \" +\n                                      _vm._s(award.description) +\n                                      \" \"\n                                  )\n                                ])\n                              ]\n                            ),\n                            _vm._v(\" \" + _vm._s(award.price_in_coins) + \" \"),\n                            _c(\"img\", {\n                              attrs: { src: __webpack_require__(/*! ./img/Coin.png */ \"./src/views/pages/img/Coin.png\") }\n                            })\n                          ]\n                        )\n                      ],\n                      1\n                    )\n                  ],\n                  1\n                )\n              ]\n            )\n          }),\n          1\n        )\n      ],\n      1\n    )\n  ])\n}\nvar staticRenderFns = []\nrender._withStripped = true\n\n\n\n//# sourceURL=webpack:///./src/views/pages/Awards.vue?./node_modules/cache-loader/dist/cjs.js?%7B%22cacheDirectory%22:%22node_modules/.cache/vue-loader%22,%22cacheIdentifier%22:%221d97a420-vue-loader-template%22%7D!./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js?!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/Awards.vue?vue&type=style&index=0&lang=css&":
/*!**********************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src??ref--6-oneOf-1-2!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/pages/Awards.vue?vue&type=style&index=0&lang=css& ***!
  \**********************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("// Imports\nvar ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../../../node_modules/css-loader/dist/runtime/api.js */ \"./node_modules/css-loader/dist/runtime/api.js\");\nexports = ___CSS_LOADER_API_IMPORT___(false);\n// Module\nexports.push([module.i, \"\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n  /* .card-columns {\\n    width: 70%;\\n    margin: auto;\\n    margin-top: 130px;\\n    border-radius: 20px;\\n  } */\\n\\n  /* .card-img {\\n    width: 100%;\\n    height: auto\\n  } */\\n.bg-secondary {\\n    background: transparent !important;\\n    border-radius: 18px !important;\\n    border: 2px solid #EBEDF0;\\n-webkit-box-shadow: 0px 2px 0px #CFD8DA;\\n        box-shadow: 0px 2px 0px #CFD8DA;\\n}\\n.bg-secondary:hover {\\n     border: 2px solid rgba(153,162,173, 0.1);\\n}\\n.hover:hover {\\n    background-color: rgba(153,162,173, 0.1) !important;\\n    border: none;\\n}\\n.wrapper {\\n    border-radius: 18px;\\n}\\n.award_card:hover {\\n    background: rgba(153,162,173, 0.1) !important;\\n    border-radius: 18px;\\n    cursor: pointer;\\n}\\n\", \"\"]);\n// Exports\nmodule.exports = exports;\n\n\n//# sourceURL=webpack:///./src/views/pages/Awards.vue?./node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src??ref--6-oneOf-1-2!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "./node_modules/vue-style-loader/index.js?!./node_modules/css-loader/dist/cjs.js?!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/Awards.vue?vue&type=style&index=0&lang=css&":
/*!************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/vue-style-loader??ref--6-oneOf-1-0!./node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src??ref--6-oneOf-1-2!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/pages/Awards.vue?vue&type=style&index=0&lang=css& ***!
  \************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("// style-loader: Adds some css to the DOM by adding a <style> tag\n\n// load the styles\nvar content = __webpack_require__(/*! !../../../node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!../../../node_modules/vue-loader/lib/loaders/stylePostLoader.js!../../../node_modules/postcss-loader/src??ref--6-oneOf-1-2!../../../node_modules/cache-loader/dist/cjs.js??ref--0-0!../../../node_modules/vue-loader/lib??vue-loader-options!./Awards.vue?vue&type=style&index=0&lang=css& */ \"./node_modules/css-loader/dist/cjs.js?!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/Awards.vue?vue&type=style&index=0&lang=css&\");\nif(content.__esModule) content = content.default;\nif(typeof content === 'string') content = [[module.i, content, '']];\nif(content.locals) module.exports = content.locals;\n// add the styles to the DOM\nvar add = __webpack_require__(/*! ../../../node_modules/vue-style-loader/lib/addStylesClient.js */ \"./node_modules/vue-style-loader/lib/addStylesClient.js\").default\nvar update = add(\"0c197e3d\", content, false, {\"sourceMap\":false,\"shadowMode\":false});\n// Hot Module Replacement\nif(false) {}\n\n//# sourceURL=webpack:///./src/views/pages/Awards.vue?./node_modules/vue-style-loader??ref--6-oneOf-1-0!./node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src??ref--6-oneOf-1-2!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options");

/***/ }),

/***/ "./src/views/pages/Awards.vue":
/*!************************************!*\
  !*** ./src/views/pages/Awards.vue ***!
  \************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _Awards_vue_vue_type_template_id_0b2caf1b___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./Awards.vue?vue&type=template&id=0b2caf1b& */ \"./src/views/pages/Awards.vue?vue&type=template&id=0b2caf1b&\");\n/* harmony import */ var _Awards_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./Awards.vue?vue&type=script&lang=js& */ \"./src/views/pages/Awards.vue?vue&type=script&lang=js&\");\n/* empty/unused harmony star reexport *//* harmony import */ var _Awards_vue_vue_type_style_index_0_lang_css___WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./Awards.vue?vue&type=style&index=0&lang=css& */ \"./src/views/pages/Awards.vue?vue&type=style&index=0&lang=css&\");\n/* harmony import */ var _node_modules_vue_loader_lib_runtime_componentNormalizer_js__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../../node_modules/vue-loader/lib/runtime/componentNormalizer.js */ \"./node_modules/vue-loader/lib/runtime/componentNormalizer.js\");\n\n\n\n\n\n\n/* normalize component */\n\nvar component = Object(_node_modules_vue_loader_lib_runtime_componentNormalizer_js__WEBPACK_IMPORTED_MODULE_3__[\"default\"])(\n  _Awards_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_1__[\"default\"],\n  _Awards_vue_vue_type_template_id_0b2caf1b___WEBPACK_IMPORTED_MODULE_0__[\"render\"],\n  _Awards_vue_vue_type_template_id_0b2caf1b___WEBPACK_IMPORTED_MODULE_0__[\"staticRenderFns\"],\n  false,\n  null,\n  null,\n  null\n  \n)\n\n/* hot reload */\nif (false) { var api; }\ncomponent.options.__file = \"src/views/pages/Awards.vue\"\n/* harmony default export */ __webpack_exports__[\"default\"] = (component.exports);\n\n//# sourceURL=webpack:///./src/views/pages/Awards.vue?");

/***/ }),

/***/ "./src/views/pages/Awards.vue?vue&type=script&lang=js&":
/*!*************************************************************!*\
  !*** ./src/views/pages/Awards.vue?vue&type=script&lang=js& ***!
  \*************************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _node_modules_cache_loader_dist_cjs_js_ref_12_0_node_modules_babel_loader_lib_index_js_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_Awards_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../node_modules/cache-loader/dist/cjs.js??ref--12-0!../../../node_modules/babel-loader/lib!../../../node_modules/cache-loader/dist/cjs.js??ref--0-0!../../../node_modules/vue-loader/lib??vue-loader-options!./Awards.vue?vue&type=script&lang=js& */ \"./node_modules/cache-loader/dist/cjs.js?!./node_modules/babel-loader/lib/index.js!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/Awards.vue?vue&type=script&lang=js&\");\n/* empty/unused harmony star reexport */ /* harmony default export */ __webpack_exports__[\"default\"] = (_node_modules_cache_loader_dist_cjs_js_ref_12_0_node_modules_babel_loader_lib_index_js_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_Awards_vue_vue_type_script_lang_js___WEBPACK_IMPORTED_MODULE_0__[\"default\"]); \n\n//# sourceURL=webpack:///./src/views/pages/Awards.vue?");

/***/ }),

/***/ "./src/views/pages/Awards.vue?vue&type=style&index=0&lang=css&":
/*!*********************************************************************!*\
  !*** ./src/views/pages/Awards.vue?vue&type=style&index=0&lang=css& ***!
  \*********************************************************************/
/*! no static exports found */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _node_modules_vue_style_loader_index_js_ref_6_oneOf_1_0_node_modules_css_loader_dist_cjs_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_Awards_vue_vue_type_style_index_0_lang_css___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../node_modules/vue-style-loader??ref--6-oneOf-1-0!../../../node_modules/css-loader/dist/cjs.js??ref--6-oneOf-1-1!../../../node_modules/vue-loader/lib/loaders/stylePostLoader.js!../../../node_modules/postcss-loader/src??ref--6-oneOf-1-2!../../../node_modules/cache-loader/dist/cjs.js??ref--0-0!../../../node_modules/vue-loader/lib??vue-loader-options!./Awards.vue?vue&type=style&index=0&lang=css& */ \"./node_modules/vue-style-loader/index.js?!./node_modules/css-loader/dist/cjs.js?!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/Awards.vue?vue&type=style&index=0&lang=css&\");\n/* harmony import */ var _node_modules_vue_style_loader_index_js_ref_6_oneOf_1_0_node_modules_css_loader_dist_cjs_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_Awards_vue_vue_type_style_index_0_lang_css___WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_vue_style_loader_index_js_ref_6_oneOf_1_0_node_modules_css_loader_dist_cjs_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_Awards_vue_vue_type_style_index_0_lang_css___WEBPACK_IMPORTED_MODULE_0__);\n/* harmony reexport (unknown) */ for(var __WEBPACK_IMPORT_KEY__ in _node_modules_vue_style_loader_index_js_ref_6_oneOf_1_0_node_modules_css_loader_dist_cjs_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_Awards_vue_vue_type_style_index_0_lang_css___WEBPACK_IMPORTED_MODULE_0__) if([\"default\"].indexOf(__WEBPACK_IMPORT_KEY__) < 0) (function(key) { __webpack_require__.d(__webpack_exports__, key, function() { return _node_modules_vue_style_loader_index_js_ref_6_oneOf_1_0_node_modules_css_loader_dist_cjs_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_Awards_vue_vue_type_style_index_0_lang_css___WEBPACK_IMPORTED_MODULE_0__[key]; }) }(__WEBPACK_IMPORT_KEY__));\n\n\n//# sourceURL=webpack:///./src/views/pages/Awards.vue?");

/***/ }),

/***/ "./src/views/pages/Awards.vue?vue&type=template&id=0b2caf1b&":
/*!*******************************************************************!*\
  !*** ./src/views/pages/Awards.vue?vue&type=template&id=0b2caf1b& ***!
  \*******************************************************************/
/*! exports provided: render, staticRenderFns */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _node_modules_cache_loader_dist_cjs_js_cacheDirectory_node_modules_cache_vue_loader_cacheIdentifier_1d97a420_vue_loader_template_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_Awards_vue_vue_type_template_id_0b2caf1b___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! -!../../../node_modules/cache-loader/dist/cjs.js?{\"cacheDirectory\":\"node_modules/.cache/vue-loader\",\"cacheIdentifier\":\"1d97a420-vue-loader-template\"}!../../../node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!../../../node_modules/cache-loader/dist/cjs.js??ref--0-0!../../../node_modules/vue-loader/lib??vue-loader-options!./Awards.vue?vue&type=template&id=0b2caf1b& */ \"./node_modules/cache-loader/dist/cjs.js?{\\\"cacheDirectory\\\":\\\"node_modules/.cache/vue-loader\\\",\\\"cacheIdentifier\\\":\\\"1d97a420-vue-loader-template\\\"}!./node_modules/vue-loader/lib/loaders/templateLoader.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/views/pages/Awards.vue?vue&type=template&id=0b2caf1b&\");\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"render\", function() { return _node_modules_cache_loader_dist_cjs_js_cacheDirectory_node_modules_cache_vue_loader_cacheIdentifier_1d97a420_vue_loader_template_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_Awards_vue_vue_type_template_id_0b2caf1b___WEBPACK_IMPORTED_MODULE_0__[\"render\"]; });\n\n/* harmony reexport (safe) */ __webpack_require__.d(__webpack_exports__, \"staticRenderFns\", function() { return _node_modules_cache_loader_dist_cjs_js_cacheDirectory_node_modules_cache_vue_loader_cacheIdentifier_1d97a420_vue_loader_template_node_modules_vue_loader_lib_loaders_templateLoader_js_vue_loader_options_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_Awards_vue_vue_type_template_id_0b2caf1b___WEBPACK_IMPORTED_MODULE_0__[\"staticRenderFns\"]; });\n\n\n\n//# sourceURL=webpack:///./src/views/pages/Awards.vue?");

/***/ }),

/***/ "./src/views/pages/img/Coin.png":
/*!**************************************!*\
  !*** ./src/views/pages/img/Coin.png ***!
  \**************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("module.exports = \"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAYAAADgKtSgAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAKxSURBVHgBlVTdThNBFD4zs7bld2kREhKNxUhighdtvCDEG7gzCIk+gTwCb1B5BN/AN1AjId6VG2y4MHIBV9VY1ESF9Nc2dKGz4znb7DLTbZfyJbCdOed858z5Y3ANqoX1FVAqw7lKMxC2All3XVbCu73kk93DKFs2SFA/WM/hZwsVpgbpKFAl11XbyeXdN0ORVwtP05yLPAOWhiHRdSJXk8sfSwPJq/trGW7xfFS0EajJjruqp4qZEVtfeokbzUs4Lbeh3rzwzpZgMDZiwez0CEyO3wo7cDtZ/wWWf9tNxRVx+0LCt5N/AakPB/9a5x04rbRhNpWAu3NjEI8JXzzFhXiL36zH2Y16bVPPMREfF2sh4l6QgyPUc1A/SIVimeqnZ1sBOecspxuVfjUNgyiQXvGkYdxxAS89R9THgkPeF1COj4pVQzllx2BuZjQg+/mnhV/X0FlcmAJ7PBacsbhZnA2W0ZX+ls9D0aXsBIyNWnBWccCeiMGDe5MhnTMsuhE9YysccPL0SyrWINSbDrQdiR3D+8guzQvk5TgBRutJqfoSE+HjxduQiFuhHPcDrQoL/9dgCFCuPx+XB8qp/3XQDuJAS0iDHR6MoUCDZQB5ucuUsdlmphMhQ+qOH79bEIWZlGnn4tb03tI42MDeU0HuqRUbvQWKQMqOw8P7tnbDSpNLH+a9sitXvdaVqdXiMT4UMenN3xk3L13Y9lz4Z4z+O7pJ+2daAV+xK6JeQItrwQtEhKKmX0EVZEe8EJbM++lJoMGjhSSUaw5U6o7X/1J2p5ImkXJMA2WC4VYUq8FJF1X3n2d0BzcDEncE7vN3QYMYiSUBes7S0+AGYAw8O504FLmORmFjE13n9DqESdWhq9h7e2nnVV85XIMmpkoyuUK7guGqUDTRNCBIPLG8sxdl+x9NKCXGfRfStgAAAABJRU5ErkJggg==\"\n\n//# sourceURL=webpack:///./src/views/pages/img/Coin.png?");

/***/ })

}]);