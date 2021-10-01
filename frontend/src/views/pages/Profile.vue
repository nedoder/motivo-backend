<template>
 <CWrapper>
    <TheHeader/>
<div class="formcontainer">
   
</div>
 </CWrapper>
</template>

<script>
import TheHeader from '../../containers/TheHeader.vue'
import axios from 'axios'
import forms from '@/mixins/forms';

export default {
  name:"Profile",
  components: {TheHeader,},
  data(){
    return {
       
    }
  },

  mixins: [ forms ],

  // @todo please use one empty line to separate elements like data, mixins, methods, mounted...
  methods:{
    // @todo my version


      
  },
}


 
</script>

<style scoped>
 form {
   width: 100%;
 }

 .formcontainer {
   width: 40%;
   margin: auto;
   margin-top: 15%;
  }
 h4 {
   text-align: center;
   padding-bottom: 1rem;
 }
 a {
   color: #1CB0F6;
   font-weight: bold;
 }

 input, button {
   border-radius: 12px;
   padding: 10px;
 }

 button {
     color: #1CB0F6;
     font-weight: bold;
 }
</style>