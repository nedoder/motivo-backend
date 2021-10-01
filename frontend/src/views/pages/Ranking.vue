<template>
  <CRow>
    <CCol col="12" xl="12" sm="12">
      <CRow v-bind:style="{borderRadius: '18px', border: '2px solid #EBEDF0', padding: '10px', margin: '10px' }">
        <!-- <CCol col="12" sm="12">
          <CCardBody> -->
            <!-- <CJumbotron class='bg-light' text-color="info" border-color="info"> -->
              <CCol>
              <img src="./img/Ellipse 23.png" v-bind:style="{margin: '10px'}"/>
              </CCol>
              <CCol>
              <p v-bind:style="{color: '#B8C1CC !important'}">
                Place:  
              </p>
              <h5 v-bind:style="{color: '#03001D !important'}">
                {{count}}
              </h5>
              </CCol>
              <CCol>
              <p class='fs-3' v-bind:style="{color: '#B8C1CC !important'}">
                Title:
              </p>
              <h5 v-bind:style="{color: '#03001D !important'}">
                 {{userItems[0].title}}
              </h5>
              </CCol>
              <CCol>
              <p v-bind:style="{color: '#B8C1CC !important'}">
                Balance: 
              </p>
              <h5 v-bind:style="{color: '#F2C94C !important'}">{{userItems[0].collected_coins_gross}}  <img src="./img/Coin.png"/></h5>
              </CCol>
              <CCol>
              <p v-bind:style="{color: '#B8C1CC !important'}">
                Current balance: 
              </p>
              <h5 v-bind:style="{color: '#F2C94C !important'}">{{userItems[0].collected_coins}}  <img src="./img/Coin.png"/></h5>
              </CCol>
            <!-- </CJumbotron> -->
          <!-- </CCardBody>
        </CCol> -->
      </CRow>
      <CDataTable v-bind:style="{borderRadius: '18px', border: '2px solid #EBEDF0', padding: '10px', margin: '10px' }"
      hover 
      :items="collectedFilteredItems" 
      :fields="fields" 
      :items-per-page="20" 
      :header=false
      :active-page="activePage" 
      :pagination="{ doubleArrows: false, align: 'center'}"
     
       @page-change="pageChange"
      >
      </CDataTable>
    </CCol>
  </CRow>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'Ranking',
    data() {
      return {
        items: [],
        count: null,
        fields: [
          {
            key: 'count',
            label: 'Count',
            _classes: 'font-weight-bold'
          },
          
          {
            key: 'userUsername',
            label: 'User',
            _classes: 'font-weight-bold'
          },
          {
            key: 'title',
            label: 'Title'
          },
          {
            key: 'collected_coins_gross',
            label: 'Collected Coins Gross'
          },
          {
            key: 'collected_coins',
            label: 'Collected Coins'
          },
        ],
         activePage: 1
      }
    },
    computed: {
      computedItems() {
        let userid = parseInt(localStorage.getItem('user-id'))
        return this.items.map((item,index) => {
          if(item.id === userid) {
            this.count = index + 1
          }
          return {
            ...item,
            userUsername: item.first_name + ' ' + item.last_name,
            userId: item.id,
            title: item.title,
            count: index + 1,
            balance: item.collected_coins,
          }
        })
      },
      collectedFilteredItems() {
        return this.computedItems.sort(function (a, b) {
          return b.collected_coins_gross - a.collected_coins_gross
        })
      },
      userItems() {
        let userid = parseInt(localStorage.getItem('user-id'))
         return this.items.filter(item => item.id === userid) 
         
        },
    },
    watch: {
      $route: {
        immediate: true,
        handler(route) {
          if (route.query && route.query.page) {
            this.activePage = Number(route.query.page)
          }
        }
      }
    },
    methods: {
      // getBadge (status) {
      //   switch (status) {
      //     case 'Active': return 'success'
      //     case 'Inactive': return 'secondary'
      //     case 'Pending': return 'warning'
      //     case 'Banned': return 'danger'
      //     default: 'primary'
      //   }
      // rowClicked (item, index) {
      //   this.$router.push({path: `users/${index + 1}`})
      // },
      pageChange(val) {
        this.$router.push({
          query: {
            page: val
          }
        })
      }
    },
    mounted() {
      const token = localStorage.getItem('user-token')
      const bearer = 'Bearer ' + token
      axios({
          method: 'get',
          url: 'https://api.motivo.localhost/ranking/',
          headers: {
            'Authorization': bearer,
          }
        })
        .then(resp => {
          this.items = resp.data.results
          // this.title = resp.data.results[0].title
          // this.price = resp.data.results[0].price
          // this.image = resp.data.results[0].image
        })
        .catch(error => console.log(error))
    },
  }
</script>

<style>

.table td {
  border: none !important;
}

 td {
  border: none !important;
}

</style>