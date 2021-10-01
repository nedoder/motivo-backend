<template>
  <CRow class="d-flex justify-content-center">
    <CCol col="12" lg="6">
      <CCard  v-bind:style="{height: '450px', borderRadius:'18px', backgroundSize: 'cover', top:'25%'}">
        <!-- <CCardHeader class='headerCard' :style="{backgroundColor: 'transparent'}">
          <h2>Challenge: {{ this.tasks.title }}</h2>
        </CCardHeader> -->
        <CCardBody class="card-title" v-bind:style="{ color: 'black', padding: '20px 10px 10px 10px' , margin: '0px', borderRadius: '18px', backgroundColor: '#fff'}">
          <CRow class='m-3' v-bind:style="{color: '#F2C94C', fontWeight: 'bold', fontSize: '18x'}">
            {{this.tasks.coins_to_win}} <img src="./img/Coin.png"  class='mx-2' /> 
          </CRow>
          <!-- <CRow>
            <CButton disabled color="secondary" variant="pill" size="lg">To do
            </CButton>
            <CButton disabled color="info" variant="pill" size="lg">In progress
            </CButton>
            <CButton disabled color="secondary" variant="pill" size="lg">Done
            </CButton>
          </CRow> -->
          <CRow class='m-auto' v-bind:style="{ display: 'flex', position: 'relative' , width: '120px', height: '135px', clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)'}">
              <img v-bind:src="this.tasks.image" alt="Award image" v-bind:style="{ width: '100%', height: 'auto' , display: 'block', objectFit: 'cover'}"/>
            </CRow>
           <CRow class='m-3'>
             <h2>Challenge: {{ this.tasks.title }}</span></h2>
            </CRow>
          
          <CRow class='m-3'>
            <p  v-linkified>Description:<span>{{this.tasks.description}}</span></p>
          </CRow>
          <CRow class='m-3'>
              <p>Not yet approved by the admin<p/>
          </CRow>
           <CButton class="col-3 m-2" color="info" @click="goBack">Back</CButton>
        </CCardBody>
        <!-- <CCardFooter class="d-flex justify-content-center" :style="{backgroundColor: 'transparent'}"> -->
         
        <!-- </CCardFooter> -->
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Attempt',
    beforeRouteEnter(to, from, next) {
      next(vm => {
        vm.challengesOpened = from.fullPath.includes('challenges')
      })
    },
    data() {
      return {
        usersOpened: null,
        tasks: null
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

