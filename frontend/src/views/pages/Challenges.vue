<template>
  <div>
    <div class="wrapper">
      <CRow alignHorizontal="center">
        <CCol class="col-2 p-3" v-for="(category, index) in categories">
          <div
            @click="filterByCategory(category.id)"
            class="category_card challenge"
          >
            <CRow
              class="m-auto"
              v-bind:style="{
                display: 'flex',
                position: 'relative',
                width: '65px',
                height: '64px',
                clipPath:
                  'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)',
              }"
            >
              <img
                v-bind:src="category.icon"
                alt="Challenge image"
                v-bind:style="{
                  width: '100%',
                  height: 'auto',
                  display: 'block',
                  objectFit: 'cover',
                }"
              />
            </CRow>
            <h4 class="text-center">{{ category.name | capitalize }}</h4>
          </div>
        </CCol>
      </CRow>

      <hr :style="[{ width: '85%' }]" />

      <CRow alignHorizontal="center" class="mb-3">
        <div
          class="row"
          :class="{
            'row-cols-3': challenges.length >= 3,
            'row-cols-2': challenges.length == 2,
            'row-cols-1': challenges.length == 1,
          }"
        >
          <CCol v-for="(challenge, index) in challenges">
            <!-- <Title text="To do" class="font-weight-bold" :number="toDo" activeColor="dark" v-bind:style="{borderRadius: '18px', border: '2px solid #EBEDF0'}"/> -->
            <div class="col-lg ">
              <div
                @click="onChallengeClicked(challenge)"
                class="challenge_card challenge mx-auto"
                :style="[
                  challenge.attempts_left === 0
                    ? { background: 'rgba(153,162,173, 0.2)' }
                    : { background: 'transparent' },
                ]"
              >
                <CRow class="coins">
                  <div>
                    <p class="coin_text">
                      {{ challenge.coins_to_win }} &nbsp;
                      <img class="text-info" src="./img/Coin.png" />
                    </p>
                  </div>
                  <div>
                    <p
                      class="attempts_text"
                      v-c-tooltip="
                        `You can try ${challenge.attempts_left} more times`
                      "
                    >
                      <font-awesome-icon icon="redo" />
                      {{ challenge.attempts_left }}
                    </p>
                    <CIcon name="cil-loop-circular" /></div
                ></CRow>
                <CRow
                  class="m-auto"
                  v-bind:style="{
                    display: 'flex',
                    position: 'relative',
                    width: '65px',
                    height: '64px',
                    clipPath:
                      'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)',
                  }"
                >
                  <img
                    v-bind:src="challenge.image"
                    alt="Challenge image"
                    v-bind:style="{
                      width: '100%',
                      height: 'auto',
                      display: 'block',
                      objectFit: 'cover',
                    }"
                  />
                </CRow>
                <h3 class="w-100">{{ challenge.title }}</h3>
                <div
                  :style="[
                    challenge.description
                      ? { visibility: 'visible' }
                      : { visibility: 'hidden' },
                  ]"
                  class="w-100 px-1"
                  style="height: 40px"
                >
                  {{ challenge.description | shortenString(50) }}
                </div>

                <!-- Active / Inactiva icon to see if the challenge is available to participate -->
                <CButton
                  class="challenge-icon"
                  v-c-tooltip="{
                    content: 'Active - you can participate in the challenge',
                    placement: 'bottom',
                  }"
                  :color="
                    challenge.challenge_available_to_attempt
                      ? 'success'
                      : 'danger'
                  "
                  :disabled="true"
                  :style="[
                    { position: 'absolute' },
                    { bottom: '5px' },
                    { right: '5px' },
                  ]"
                >
                  <span v-if="challenge.challenge_available_to_attempt">
                    A
                  </span>
                  <span v-else> I </span>
                </CButton>
              </div>
            </div>
          </CCol>
        </div>
      </CRow>
    </div>

    <challenge-details
      v-if="showModal"
      :challenge="selectedChallenge"
      :modalTitle="modalTitle"
      @closed="showModal = false"
      @submitted="onChallengeSubmitted()"
    ></challenge-details>

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
import Title from "./elements/Title.vue";
import TheHeader from "../../containers/TheHeader.vue";
import ChallengeDetails from "./ChallengeDetails.vue";
import axios from "axios";

export default {
  name: "Challenges",
  components: {
    Title,
    TheHeader,
    ChallengeDetails,
  },
  data() {
    return {
      challenges: [],
      attempts: [],
      complets: [],
      categories: [],
      toDo: null,
      failed: null,
      passed: null,
      counter: null,

      showModal: false,
      modalTitle: "",
      selectedChallenge: null,
      selectedChallengeCategoryFilter: null,

      toastMessages: [],
    };
  },
  computed: {
    computedItems() {
      return this.complets.map((item) => {
        return {
          ...item,
          challengeTitle: item.challenge.title,

          //userId: item.user.id
        };
      });
    },
  },
  mounted() {
    this.initializeComponent();
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
    /**
     * Retrieve challenges when user picks one category of challenges
     */
    filterByCategory(category_id) {
      this.selectedChallengeCategoryFilter = category_id;
      this.initializeComponent();
    },

    /**
     * Download all the component data regarding challenges
     */
    initializeComponent() {
      const token = localStorage.getItem("user-token");
      const bearer = "Bearer " + token;

      const challenges = axios({
        method: "get",
        url: "https://api.motivo.localhost/challenges/",
        headers: {
          Authorization: bearer,
        },
        params: this.axiosChallengeCategoryParams,
      });

      const attempts = axios({
        method: "get",
        url: "https://api.motivo.localhost/attempt/",
        headers: {
          Authorization: bearer,
        },
      });

      const complets = axios({
        method: "get",
        url: "https://api.motivo.localhost/completed/",
        headers: {
          Authorization: bearer,
        },
      });

      const categories = axios({
        method: "get",
        url: "https://api.motivo.localhost/categories/",
        headers: {
          Authorization: bearer,
        },
      });

      Promise.all([challenges, attempts, complets, categories])
        .then(([chal, att, com, categs]) => {
          this.attempts = att.data.results;
          this.failed = att.data.results.length;
          this.challenges = chal.data;

          console.log(this.challenges);

          // console.log("Chal" + chal.data);
          // this.challenges.sort(function (a, b) {
          //   return a.attempts_left - b.attempts_left;
          // });
          this.toDo = chal.data.length;
          this.complets = com.data.results;
          this.passed = com.data.results.length;

          this.categories = categs.data;
        })
        .catch((error) => console.log(error));
    },

    /**
     * Run when user submits the challenge successfully and the modal is closed
     */
    onChallengeSubmitted() {
      this.closeModal();
      this.addToastMessage(
        "Challenge taken",
        "Thanks for taking the challenge! Now let's wait for the approval from the admin :)\nMaybe another challenge now?",
        "success"
      );

      // Download challenge data again
      this.initializeComponent();
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

    /**
     * When challenge is clicked display modal with details - only if challenge is available
     */
    onChallengeClicked(challenge) {
      if (
        challenge.attempts_left > 0 &&
        challenge.challenge_available_to_attempt
      ) {
        this.selectedChallenge = challenge;
        this.modalTitle = challenge.title;
        this.showModal = true;
      } else {
        this.addToastMessage(
          "Challenge unavailable",
          "You can not participate in this challenge at the moment. The challenge is not active.",
          "danger"
        );
      }
    },
    completedClicked(completed) {
      this.$router.push({
        path: `/dashboard/challenges/completed/${completed.id}`,
      });
    },
    attemptClicked(attempt) {
      this.$router.push({
        path: `/dashboard/challenges/attempt/${attempt.id}`,
      });
    },
    closeModal(status, evt, accept) {
      this.showModal = false;
    },

    //     pageChange (val) {
    //       this.$router.push({ query: { page: val }})
    //     }
  },
  computed: {
    countRate: function () {
      return Math.round(
        (this.toDo / (this.failed + this.toDo + this.passed)) * 100
      );
    },
    axiosChallengeCategoryParams() {
      const params = new URLSearchParams();
      params.append("category_id", this.selectedChallengeCategoryFilter);
      return params;
    },
  },

  filters: {
    shortenString: function (value, size) {
      if (!value) return "";
      if (value.length > size) {
        return value.slice(0, size) + "...";
      } else {
        return value;
      }
    },
    capitalize: function (value) {
      if (!value) return "";
      value = value.toString();
      return value.toUpperCase();
    },
  },
};
</script>

<style scoped>
h1 {
  font-size: 36px;
  color: #03001d;
  word-wrap: break-word;
}

.challenge_card {
  border: 2px solid #ebedf0;
  box-shadow: 0px 2px 0px #cfd8da;
  border-radius: 18px;
  padding: 15px;
  margin-top: 25px;
  height: 250px;
  min-width: 25vw;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
}

.category_card {
  border: 2px solid #ebedf0;
  box-shadow: 0px 2px 0px #cfd8da;
  border-radius: 18px;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
}

.challenge_card:hover,
.category_card:hover {
  background-color: rgba(153, 162, 173, 0.2) !important;
  cursor: pointer;
}

p:first-child {
  color: #6d7885;
  font-size: 16px;
}

.coin_text {
  color: #f2c94c !important;
  margin: 0 10px;
  font-weight: bold;
  font-size: 24px;
  display: flex;
  align-items: center;
  justify-content: left;
  position: absolute;
  top: 3px !important;
  left: 3px !important;
}

.coins {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.attempts_text {
  font-weight: bold;
  position: absolute;
  top: 5px !important;
  right: 5px !important;
  color: rgb(114, 178, 218) !important;
  opacity: 0.8;
}

.col {
  padding-left: 0;
  padding-right: 0;
}

.challenge-icon {
  padding: 3px 8px;
}
</style>