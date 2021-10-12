<template>
  <CRow>
    <CCol col="12" xl="12" sm="12">
      <!-- Top data elipse -->
      <CRow
        v-bind:style="{
          borderRadius: '18px',
          border: '2px solid #EBEDF0',
          padding: '10px',
          margin: '10px',
        }"
      >
        <!-- <CCol col="12" sm="12">
          <CCardBody> -->
        <!-- <CJumbotron class='bg-light' text-color="info" border-color="info"> -->
        <CCol>
          <img src="./img/Ellipse 23.png" v-bind:style="{ margin: '10px' }" />
        </CCol>
        <CCol>
          <p v-bind:style="{ color: '#B8C1CC !important' }">Place:</p>
          <h5 v-bind:style="{ color: '#03001D !important' }">
            {{ position }}
          </h5>
        </CCol>
        <CCol>
          <p class="fs-3" v-bind:style="{ color: '#B8C1CC !important' }">
            Title:
          </p>
          <h5 v-bind:style="{ color: '#03001D !important' }">
            {{ userItems[0].title }}
          </h5>
        </CCol>
        <CCol>
          <p v-bind:style="{ color: '#B8C1CC !important' }">Balance:</p>
          <h5 v-bind:style="{ color: '#F2C94C !important' }">
            {{ userItems[0].collected_coins_gross }}
            <img src="./img/Coin.png" />
          </h5>
        </CCol>
        <CCol>
          <!-- <p v-bind:style="{color: '#B8C1CC !important'}">
                Current balance: 
              </p> -->
          <!-- <h5 v-bind:style="{color: '#F2C94C !important'}">{{userItems[0].collected_coins}}  <img src="./img/Coin.png"/></h5> -->
        </CCol>
        <!-- </CJumbotron> -->
        <!-- </CCardBody>
        </CCol> -->
      </CRow>

      <CDataTable
        id="ranking-table"
        v-bind:style="{
          borderRadius: '18px',
          border: '2px solid #EBEDF0',
          padding: '10px',
          margin: '10px',
        }"
        :items="collectedFilteredItems"
        :fields="fields"
        :items-per-page="20"
        :header="true"
        :active-page="activePage"
        :pagination="{ doubleArrows: false, align: 'center' }"
        @page-change="pageChange"
      >
        
        <template #position="{ item, index }">
          <font-awesome-icon v-if="index < 3 && activePage === 1" icon="medal" class="ml-4 mt-2" 
          v-bind:style="{fontSize: '1.5em'}" 
          :class="index==0 ? 'golden' : index == 1 ? 'silver' : 'bronze' " />

          <template v-if="activePage > 1 || (activePage === 1 && index > 2)">
            <b class="ml-4" > {{ item.position }} </b>
          </template>
        </template>

      </CDataTable>
    </CCol>
  </CRow>
</template>

<script>
import { dom } from "@fortawesome/fontawesome-svg-core";

import axios from "axios";
export default {
  name: "Ranking",
  data() {
    return {
      items: [],
      position: null,
      fields: [
        {
          key: "position",
          label: "Position",
          _classes: "font-weight-bold",
        },

        {
          key: "userUsername",
          label: "User",
          _classes: "font-weight-bold",
        },
        {
          key: "title",
          label: "Title",
        },
        {
          key: "collected_coins_gross",
          label: "Historically earned coins",
        },
        // {
        //   key: 'collected_coins',
        //   label: 'Collected Coins'
        // },
      ],
      activePage: 1,
    };
  },
  computed: {
    computedItems() {
      let userid = parseInt(localStorage.getItem("user-id"));
      return this.items.map((item, index) => {
        if (item.id === userid) {
          this.position = index + 1;
        }
        return {
          ...item,
          userUsername: item.first_name + " " + item.last_name,
          userId: item.id,
          title: item.title,
          position: index + 1,
          balance: item.collected_coins,
        };
      });
    },
    collectedFilteredItems() {
      return this.computedItems.sort(function (a, b) {
        return b.collected_coins_gross - a.collected_coins_gross;
      });
    },
    collectedFilteredItems2() {
      return this.computedItems.sort(function (a, b) {
        return b.collected_coins_gross;
      });
    },
    userItems() {
      let userid = parseInt(localStorage.getItem("user-id"));
      return this.items.filter((item) => item.id === userid);
    },
  },
  watch: {
    $route: {
      immediate: true,
      handler(route) {
        if (route.query && route.query.page) {
          this.activePage = Number(route.query.page);
        }
      },
    },
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
    // setupMedals() {
    //   var rows = document.getElementsByTagName("table")[0].rows;
    //   console.log("---");
    //   console.log(rows[1].cells);
    //   console.log(rows[1].cells[0]);
    //   console.log(rows[1].cells[0].innerHTML);

    //   var html_to_insert = '<font-awesome-icon icon="medal" />';

    //   rows[1].cells[0].innerHTML = html_to_insert;
    //   rows[2].cells[0].innerHTML = html_to_insert;
    //   rows[3].cells[0].innerHTML = html_to_insert;

    //   console.log(console.log(rows[1].cells[0].innerHTML));
    //   dom.watch();
    // },
    pageChange(val) {
      this.$router.push({
        query: {
          page: val,
        },
      });
    },
  },
  mounted() {
    const token = localStorage.getItem("user-token");
    const bearer = "Bearer " + token;
    axios({
      method: "get",
      url: "https://api.motivo.localhost/ranking/",
      headers: {
        Authorization: bearer,
      },
    })
      .then((resp) => {
        this.items = resp.data.results;
        // this.title = resp.data.results[0].title
        // this.price = resp.data.results[0].price
        // this.image = resp.data.results[0].image
      })
      .catch((error) => console.log(error));
  },
  updated() {
    // this.setupMedals();
  },
};
</script>

<style>
.table td {
  border: none !important;
}

td {
  border: none !important;
}

.golden {
  color: gold;
}

.silver {
  color: silver;
}

.bronze {
  color: #803232;
}

</style>