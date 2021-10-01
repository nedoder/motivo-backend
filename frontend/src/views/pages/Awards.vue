<template>
  <div>
    <div class="wrapper">
    <CRow fluid>
      
      <CCol v-for="award in awards" sm="4" v-bind:style="{padding:'1px'}">
        <div  class="award_card">
        <CCard class='bg-secondary' @click="award.awards_left===0 ? null : couponClicked(award)" :style= "[award.awards_left===0 ? {background:'rgba(153,162,173, 0.2)', borderRadius: '18px !important'} : {background: 'transparent', borderRadius: '18px !important'}]">
          <!-- <CCardHeader class='bg-info'>
           
          </CCardHeader> --> 
          <CCardBody class='hover' v-bind:style="{color: '#F2C94C', padding:'50px 10px 10px 10px', fontWeight: 'bold', height: '250px', margin: '0px', borderRadius: '18px', fontSize: '24px', background: 'transparent'}">
            <div v-bind:style="{color: '#03001D', margin: '2px 0'}">
             <h2 v-bind:style="{fontSize: '1.5em'}">{{award.title}}</h2>
            </div>
            <div v-bind:style="{color: '#03001D', fontSize: '16px', fontWeight: '500', marginTop: '20px'}">
              <h6 v-bind:style="{color: '#6D7885'}">
            Awards left: {{award.awards_left}}
              </h6>
            </div>
            <div v-bind:style="{color: '#6D7885', fontSize: '14px', fontWeight: '400', marginTop: '20px'}">
              <p>
            Description: {{award.description}}
              </p>
            </div>
            {{award.price_in_coins}} <img src="./img/Coin.png" /> 
          </CCardBody>
          <!-- <CCardFooter class='bg-secondary'>
            Description: {{award.description}} 
          </CCardFooter> -->
        </CCard>
        </div>
      </CCol>
      <!-- <CCol sm="6">
      </CCol> -->
     
    </CRow>
     </div>
    
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Awards',
    
    data() {
      return {
        awards: []
      }
    },
    //   watch: {
    //     $route: {
    //       immediate: true,
    //       handler (route) {
    //         if (route.query && route.query.page) {
    //           this.activePage = Number(route.query.page)
    //         }
    //       }
    //     }
    //   },
    //   methods: {
    //     getBadge (status) {
    //       switch (status) {
    //         case 'Active': return 'success'
    //         case 'Inactive': return 'secondary'
    //         case 'Pending': return 'warning'
    //         case 'Banned': return 'danger'
    //         default: 'primary'
    //       }
    //     },
    //     rowClicked (item, index) {
    //       this.$router.push({path: `users/${index + 1}`})
    //     },
    //     pageChange (val) {
    //       this.$router.push({ query: { page: val }})
    //     }
    //   }

    mounted() {
      const token = localStorage.getItem('user-token')
      const bearer = 'Bearer ' + token
      axios({
          method: 'get',
          url: 'https://api.motivo.localhost/awards/',
          headers: {
            'Authorization': bearer,
          }
        })
        .then(resp => {
          this.awards = resp.data
           this.awards.sort(function (a, b) {
              return a.awards_left - b.awards_left
        })
          // this.title = resp.data.results[0].title
          // this.price = resp.data.results[0.].price
          // this.image = resp.data.results[0].image
          console.log(resp.data[0])
        })
        .catch(error => console.log(error))
    },

    methods: {

      couponClicked(award) {
                this.$router.push({
                    path: `/dashboard/awards/${award.id}`
                   
                })
            },
    }
  }
</script>

<style>
  /* .card-columns {
    width: 70%;
    margin: auto;
    margin-top: 130px;
    border-radius: 20px;
  } */

  /* .card-img {
    width: 100%;
    height: auto
  } */

  .bg-secondary {
    background: transparent !important;
    border-radius: 18px !important;
    border: 2px solid #EBEDF0;
box-shadow: 0px 2px 0px #CFD8DA;
   }

   .bg-secondary:hover {
     border: 2px solid rgba(153,162,173, 0.1);
   }

  .hover:hover {
    background-color: rgba(153,162,173, 0.1) !important;
    border: none;
  }
  
  .wrapper {
    border-radius: 18px;
  }

  .award_card:hover {
    background: rgba(153,162,173, 0.1) !important;
    border-radius: 18px;
    cursor: pointer;
}
</style>