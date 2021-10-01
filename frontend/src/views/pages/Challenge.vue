<template>
  <CRow class="d-flex justify-content-center">
    <CCol col="12" lg="6">
      <form @submit.prevent="submitForm" >
        <CCard class='forImage'  v-bind:style="{ color: 'black', padding: '10px' , margin: '0px', borderRadius: '18px', backgroundColor: '#fff', top: '10px'}">
          
          <CCardBody class="card-title">
          <!-- <div class='bodyCard'> -->
          <!-- <CCardHeader class='headerCard' :style="{backgroundColor: 'rgba(153,162,173, 0.9)'}"> -->
             <CRow class='m-3'>
            <p class='coin_text'> {{this.tasks.coins_to_win }} &nbsp; <img class="text-info" src="./img/Coin.png" /></p>
            </CRow>
            <CRow class='m-auto' v-bind:style="{ display: 'flex', position: 'relative' , width: '120px', height: '135px', clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)'}">
              <img v-bind:src="this.tasks.image" alt="Award image" v-bind:style="{ width: '100%', height: 'auto' , display: 'block', objectFit: 'cover'}"/>
            </CRow>
            <CRow class='m-3'>
            <h2>{{this.tasks.title}}</h2>
            </CRow>
           
          <!-- </CCardHeader> -->
          
            <!-- <div class='textBox text'> -->
              <CRow class='m-3'>
              <p>Description:</p>
              <p  v-linkified> {{this.tasks.description}}</p>
              </CRow>
            <!-- </div>
            <div class='textBox text'> -->
              <CRow class='m-3'>
              <p>
                Your comment
              </p>
              </CRow>
              <CRow class='m-3'>
              <textarea v-model="description"  required />
              </CRow>
              <!-- </div>
      <div class='textBox text'>  -->
        <CRow class='m-3'>
  <p >
                Attach file 
							</p>
        </CRow>
              <CRow class='m-3'>
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        </CRow>
 <!-- </div>

        </div> -->
        <CCardFooter class="d-flex justify-content-center" :style="{backgroundColor: 'transparent'}">
          <CButton color="info" @click="goBack">Back</CButton>
          <CButton color="info" type="submit">Submit</CButton>        
          </CCardFooter>
          </CCardBody>
      </CCard>
      </form>
    </CCol>
  </CRow>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'Challenge',
    beforeRouteEnter(to, from, next) {
      next(vm => {
        vm.challengesOpened = from.fullPath.includes('challenges')
      })
    },
    data() {
      return {
        usersOpened: null,
        tasks: null,
        description: '', 
        file: '',
      }
    },
    computed: {
      challengeData() {
        const id = this.$route.params.id
        const task = this.challenges.find((task, index) => index + 1 == id)
        const taskDetails = task ? Object.entries(task) : [
          ['id', 'Not found']
        ]
        return taskDetails.map(([key, value]) => {
          return {
            key,
            value
          }
        })
      },
    },
    methods: {
      goBack() {
        this.$router.push({
          path: '/dashboard/challenges'
        })
      },
      handleFileUpload(){
    this.file = this.$refs.file.files[0];
    console.log(this.file)
  },
      submitForm() {
        const token = localStorage.getItem('user-token')
        const bearer = 'Bearer ' + token
        let formData = new FormData();
        formData.append('file', this.file);
         formData.append('user',localStorage.getItem('user-id'));
         formData.append('challenge', this.$route.params.id);
          formData.append('description', this.description);
        axios({
            method: 'post',
            url: 'https://api.motivo.localhost/attempt/',
            data: formData,
            headers: {
            'Authorization': bearer,
            'Content-Type': 'multipart/form-data',
             }
          }).then(response => {
        alert("You uploaded your solution successfully!")
      this.$router.push('/dashboard/challenges')
       console.log(response)
      }).catch(error => {
        alert("Something went wrong! Please try again.")
        console.log(error)
      })
    }
    },
    mounted() {
      const token = localStorage.getItem('user-token')
      const bearer = 'Bearer ' + token
      const tasks = axios({
        method: 'get',
        url: `https://api.motivo.localhost/challenges/${this.$route.params.id}`,
        headers: {
          'Authorization': bearer,
        }
      });
      Promise.all([tasks]).then(([chal]) => {
        this.tasks = chal.data;
        console.log(this.tasks)
      }).catch(error => console.log(error))
//POST /api/attempt/
      // {
//       "user": {
//         "username": "nedoder1",
//         "id": 1
//       },
//       "challenge": {
//         "title": "test",
//         "id": 1,
//         "coins": 3,
//         "description": "ddjjd"
//       },
//       "file": null,
//       "confirmed_by_admin": false
//     },
    },
    
  }
</script>

<style scoped>
button {
  color: white;
  border: none;
  width: calc(100% - 30px);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  background: #ccc;
  cursor: pointer;
  box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.3);
  transition: 0.25s all ease;
}
.active {
  background: #5968d7;
}
.coin_text {
color: #F2C94C;    
font-weight: bold;
font-size: 24px;
display: flex;
align-items: center;
justify-content: left;
margin-top: 13px;
}
pre-content {
  width: 500px;
}
.forImage {
    height: 750px;
    width: 100%;
}
.bodyCard::before {
   content: "";
    background-color: white;
      background-size: cover;
      position: absolute;
      top: 0px;
      right: 0px;
      bottom: 0px;
      left: 0px;
      opacity: 0;
}
.bodyCard {
    position: relative; 
    height: 100vh;
    width: 100%;
    display: flex;
    padding: 20px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-direction: column;
}
.text {
  position: relative;
  color: black;  
  line-height: 0.9;
  text-align: left;
}
.textBox {
  margin-top: 30px;
}
.textBox p:first-child {
  color: black;
  font-weight: bold;
}
.headerCard {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 12%;
}
textarea {
  width: auto;	
	border: none;
	border-radius: 20px;
	outline: none;
	padding: 10px 30px;
	font-size: 1em;
	color: #676767;
	box-sizing:border-box;
  height: 100px;	
	overflow: auto;
  border-radius: 18px;
  border: 1px solid #99A2AD;
}
</style>