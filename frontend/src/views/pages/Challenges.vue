<template>
  <div>
    <div class="wrapper">
      <CRow alignHorizontal="center">
        <CCol class="col-2 p-3" v-for="(category, index) in categories">
          <div class="category_card challenge">
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
        <div class="row row-cols-3">
          <CCol v-for="(challenge, index) in challenges">
            <!-- <Title text="To do" class="font-weight-bold" :number="toDo" activeColor="dark" v-bind:style="{borderRadius: '18px', border: '2px solid #EBEDF0'}"/> -->
            <div class="col-lg">
              <div
                @click="
                  challenge.attempts_left === 0
                    ? null
                    : onChallengeClicked(challenge)
                "
                class="challenge_card challenge"
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

                <CButton
                  class="challenge-icon"
                  v-c-tooltip="{
                    content: `Active - you can participate in the challenge`,
                    placement: 'bottom',
                  }"
                  color="success"
                  :disabled="true"
                  :style="[
                    { position: 'absolute' },
                    { bottom: '5px' },
                    { right: '5px' },
                  ]"
                >
                  A
                </CButton>
              </div>
            </div>
          </CCol>
        </div>
      </CRow>
    </div>

    <!-- Modal with the challenge details -->
    <CModal
      :title="modalTitle"
      color="info"
      :centered="true"
      size="lg"
      :show.sync="showModal"
      :name="'Siema!'"
    >
      <challenge-details
        v-if="showModal"
        @update:show="closeModal"
        :challenge="selectedChallenge"
      ></challenge-details>
    </CModal>
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
    const token = localStorage.getItem("user-token");
    const bearer = "Bearer " + token;
    const challenges = axios({
      method: "get",
      url: "https://api.motivo.localhost/challenges/",
      headers: {
        Authorization: bearer,
      },
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

        console.log("Chal" + chal.data);
        this.challenges.sort(function (a, b) {
          return a.attempts_left - b.attempts_left;
        });
        this.toDo = chal.data.length;
        this.complets = com.data.results;
        this.passed = com.data.results.length;

        this.categories = categs.data;
      })
      .catch((error) => console.log(error));
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
    onChallengeClicked(challenge) {
      // this.$router.push({
      //   path: `/dashboard/challenges/${challenge.id}`,
      // });
      this.selectedChallenge = challenge;
      this.modalTitle = challenge.title;
      this.showModal = true;
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