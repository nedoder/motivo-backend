<template>
<div class="wrapper-in">
<div class="motivo">
  <img src="./img/motivo.png"/>
<div class="wrapper-out">
    <div>
       <h4>Sign up</h4>
    </div>
   <form>
       <div class="form-group">
    <label for="exampleFormControlInput1">Name</label>
    <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Name">
  </div>
  <div class="form-group">
    <label for="exampleFormControlInput2">Surname</label>
    <input type="text" class="form-control" id="exampleFormControlInput2" placeholder="Surname">
  </div>
  <div class="form-group">
    <label for="exampleFormControlInput3">Email</label>
    <input type="email" class="form-control" id="exampleFormControlInput3" placeholder="Email">
  </div>
  <div class="form-group">
    <label for="exampleFormControlInput4">Password</label>
    <input type="password" class="form-control" id="exampleFormControlInput4" placeholder="Password">
  </div>
  <div class="form-group">
    <label for="exampleFormControlInput5">Invite code</label>
    <input type="text" class="form-control" id="exampleFormControlInput5" placeholder="Code">
  </div>
  <div class="form-group">
    <button type="submit" class="btn btn-info btn-lg btn-block">Sign up</button>
  </div>
  <div class="form-group">
    <button type="button" class="btn btn-link btn-lg btn-block">I don't have an account</button>
  </div>
</form>
</div>
</div>
</div>
</template>

<script>
import CustomSignUp from './CustomSignUp'
export default {
  name: 'CustomSignUp',
  components: { CustomSignUp }
}
</script>

<style scoped>
 form {
   width: 50%;
   margin: auto;
 }
 .wrapper-in {
  background: #ffffff;
    height: 100vh;
}
.wrapper-out {
  padding-top: 100px;
}
 h4 {
   text-align: center;
   font-size: 24px;
   color: #6D7885;
 }
 a, .btn-link {
   color: #1CB0F6;
   font-weight: bold;
   font-size: 18px;
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
 input, button {
   border-radius: 12px;
   padding: 10px;
 }
 input {
   font-size: 18px;
   background: #F7F8FA;
 }
 .motivo {
    width: 100%;
    margin: auto;
    padding: 30px 50px;
  }
  #exampleFormControlInput5 {
    margin-bottom: 30px;
  }
</style>