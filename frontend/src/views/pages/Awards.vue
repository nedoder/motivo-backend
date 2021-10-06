<template>
  <div>
    <div class="wrapper">
      <CRow
        alignHorizontal="start"
        :class="{
          'row-cols-3': awards.length >= 3,
          'row-cols-2': awards.length == 2,
          'row-cols-1': awards.length == 1,
        }"
      >
        <CCol class="col-2 p-3" v-for="award in awards" sm="4">
          <div class="award_card">
            <CCard
              class="bg-secondary"
              @click="award.awards_left === 0 ? null : onAwardSelected(award)"
              :style="[
                award.awards_left === 0
                  ? {
                      background: 'rgba(153,162,173, 0.2)',
                      borderRadius: '18px !important',
                    }
                  : {
                      background: 'transparent',
                      borderRadius: '18px !important',
                    },
              ]"
            >
              <!-- <CCardHeader class='bg-info'>
           
          </CCardHeader> -->
              <CCardBody
                class="hover"
                v-bind:style="{
                  color: '#F2C94C',
                  padding: '50px 10px 10px 10px',
                  fontWeight: 'bold',
                  height: '250px',
                  margin: '0px',
                  borderRadius: '18px',
                  fontSize: '24px',
                  background: 'transparent',
                }"
              >
                <div v-bind:style="{ color: '#03001D', margin: '2px 0' }">
                  <h2 v-bind:style="{ fontSize: '1.5em' }">
                    {{ award.title }}
                  </h2>
                </div>
                <div
                  v-bind:style="{
                    color: '#03001D',
                    fontSize: '16px',
                    fontWeight: '500',
                    marginTop: '20px',
                  }"
                >
                  <h6 v-bind:style="{ color: '#6D7885' }">
                    Awards left: {{ award.awards_left }}
                  </h6>
                </div>
                <div
                  v-bind:style="{
                    color: '#6D7885',
                    fontSize: '14px',
                    fontWeight: '400',
                    marginTop: '20px',
                  }"
                >
                  <p>Description: {{ award.description }}</p>
                </div>
                {{ award.price_in_coins }} <img src="./img/Coin.png" />
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

    <award-details
      v-if="showModal"
      :award="selectedAward"
      :modalTitle="modalTitle"
      :coins="coins"
      @closed="showModal = false"
      @submitted="onAwardBought()"
    ></award-details>

    <!-- Toast message to be displayed -->
    <CToaster :autohide="3000">
      <template v-for="toastMessage in toastMessages">
        <CToast
          :key="toastMessage.id"
          :show="true"
          :header="toastMessage.header"
          :color="toastMessage.color"
        >
          {{ toastMessage.content }}
        </CToast>
      </template>
    </CToaster>
  </div>
</template>

<script>
import axios from "axios";
import AwardDetails from "./AwardDetails.vue";

export default {
  name: "Awards",
  components: {
    AwardDetails,
  },

  data() {
    return {
      awards: [],
      showModal: false,
      modalTitle: "",
      selectedAward: null,
      toastMessages: [],
      coins: 0,
    };
  },
  mounted() {
    this.initializeComponent();
    this.getAmountOfCoins();
  },

  methods: {
    getAmountOfCoins() {
      const token = localStorage.getItem("user-token");
      const bearer = "Bearer " + token;
      const id = localStorage.getItem("user-id");
      axios({
        method: "get",
        url: "https://api.motivo.localhost/profile/",
        headers: {
          Authorization: bearer,
        },
      })
        .then((resp) => {
          console.log(resp);
          var results = resp.data.results;
          let userid = parseInt(localStorage.getItem("user-id"));
          results.forEach((result) => {
            if (result.id === userid) {
              this.coins = result.collected_coins;
            }
          });
          this.coins = this.coins.filter((result) => result.id === userid);
        })
        .catch((error) => console.log(error));
    },

    initializeComponent() {
      const token = localStorage.getItem("user-token");
      const bearer = "Bearer " + token;
      axios({
        method: "get",
        url: "https://api.motivo.localhost/awards/",
        headers: {
          Authorization: bearer,
        },
      })
        .then((resp) => {
          this.awards = resp.data;
          // this.awards.sort(function (a, b) {
          //   return a.awards_left - b.awards_left;
          // });
          // this.title = resp.data.results[0].title
          // this.price = resp.data.results[0.].price
          // this.image = resp.data.results[0].image
          console.log(resp.data[0]);
        })
        .catch((error) => console.log(error));
    },

    /**
     * Adds a new toast message to the array when event occurred
     */
    addToastMessage(header, content, color) {
      var id = this.toastMessages.length;
      this.toastMessages.push({
        id: id,
        header: header,
        content: content,
        color: color,
      });
    },

    onAwardSelected(award) {
      this.selectedAward = award;
      this.modalTitle = award.title;
      this.showModal = true;
    },

    closeModal() {
      this.showModal = false;
    },

    onAwardBought() {
      console.log("Award bought!");
      this.closeModal();
      this.addToastMessage(
        "Award collected",
        "You asked for collecting the award successfully. We will get in touch with you soon!",
        "success"
      );

      // Download challenge data again
      this.initializeComponent();
    },
    couponClicked(award) {
      this.$router.push({
        path: `/dashboard/awards/${award.id}`,
      });
    },
  },
};
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
  border: 2px solid #ebedf0;
  box-shadow: 0px 2px 0px #cfd8da;
}

.bg-secondary:hover {
  border: 2px solid rgba(153, 162, 173, 0.1);
}

.hover:hover {
  /* background-color: rgba(153, 162, 173, 0.1) !important; */
  border: none;
}

.wrapper {
  border-radius: 18px;
}

.award_card:hover {
  /* background: rgba(153, 162, 173, 0.1) !important; */
  transform: translateY(5px);
  border-radius: 18px;
  cursor: pointer;
}
</style>