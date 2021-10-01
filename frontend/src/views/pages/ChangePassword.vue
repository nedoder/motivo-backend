<template>
<div class="wrapper-in">
    <CWrapper>
<div class="formcontainer">
   <form>
     <div>
       <h4>Profile</h4>
    </div>
  <div class="form-group">
    <label for="exampleFormControlInput2">Email</label>
    <input type="email" class="form-control" id="exampleFormControlInput3" placeholder="Email" v-model="editInfo.email">
  </div>
  <div class="form-group">
    <label for="exampleFormControlInput2">Password</label>
    <input type="password" class="form-control" id="exampleFormControlInput4" placeholder="Password" v-model="editInfo.password">
  </div>
  
   <div class="form-group">
    <button type="button" class="btn btn-link btn-lg btn-block" v-on:click.prevent="editCustom">Change password</button>
  </div>

</form>
</div>
    </CWrapper>
</div>
</template>

<script>
import TheHeader from '../../containers/TheHeader.vue'
import axios from 'axios'
import forms from '@/mixins/forms';


export default {
  name:"ChangePassword",
  components: {TheHeader,},
  data(){
    return {
       editInfo: {
          name: localStorage.getItem('user-name') || '',
          surname: localStorage.getItem('user-surname') || '',
          email: localStorage.getItem('user-email'),
          password: '',
          token: localStorage.getItem('user-token') || null,
          id: localStorage.getItem('user-id')
        }
    }
  },

  mixins: [ forms ],

  // @todo please use one empty line to separate elements like data, mixins, methods, mounted...
  methods:{
    // @todo my version

      editCustom(){
        const data = {first_name: this.editInfo.name, last_name: this.editInfo.surname, email: this.editInfo.email, password: this.editInfo.password  };
        const token = localStorage.getItem('user-token')
        const bearer = 'Bearer ' + token
        console.log(bearer)
        axios({
            method:'put',
            url: `https://api.motivo.localhost/user/${this.editInfo.id}/`,
            data: data,
            headers: { 'Authorization': bearer },
        })
            .then(resp=>{
              console.log(resp)
              window.localStorage.clear();
              this.$router.push('/')
            })
            .catch(error => console.log(error))
            
      }
      
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
   margin-top: 10%;
  }
 h4 {
   font-size: 24px;
   color: #6D7885;
   text-align: left;
   padding-bottom: 1rem;
 }
 a, .btn-link {
   color: #1CB0F6;
   font-weight: bold;
   font-size: 18px;
 }

 input, button {
   border-radius: 12px;
   padding: 10px;
 }

 button {
     color: #1CB0F6;
     font-weight: bold;
 }
 .wrapper-in {
   height: 100vh;
   background: #ffffff;
 }
 label {
   color: #99A2AD;
   font-size: 14px;
 }
 .btn-link {
   box-shadow: 1px 1px 3px #99A2AD;
   text-decoration: none;
 }
 .btn-info {
   font-weight: bold;
 }
 
 input {
   font-size: 18px;
   background: #F7F8FA;
 }

 #exampleFormControlInput4 {
   margin-bottom: 30px;
 }
</style>