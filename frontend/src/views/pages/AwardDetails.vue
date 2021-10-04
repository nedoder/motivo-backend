<template>
  <!-- Modal with the challenge details -->
  <CModal
    :title="modalTitle"
    color="info"
    :centered="true"
    size="lg"
    :show.sync="showModal"
  >
    <div class="p-3">
      <!-- Coins image -->
      <CRow class="my-1">
        <p class="coin_text">
          {{ award.price_in_coins }} &nbsp;
          <img class="text-info" src="./img/Coin.png" />
        </p>
      </CRow>

      <!-- Name of the award -->
      <CRow class="my-1">
        <h2>{{ award.title }}</h2>
        <!-- Description of the award -->
      </CRow>

      <!-- Description of the award -->
      <CRow class="my-1">
        <p>{{ award.description }}</p>
      </CRow>

      <!-- User comment while collecting an award -->
      <CRow class="my-1">
        <CTextarea
          label="Your comment to the award"
          class="w-100"
          v-model="note"
          placeholder="Size / color / customization ..."
          required
        />
      </CRow>
    </div>

    <!-- Overwritten footer style -->
    <template #footer>
      <div class="w-100 d-flex justify-content-between">
        <CButton @click="closeModal('close')" color="danger">Cancel</CButton>
        <CButton
          @click="collectAward()"
          color="success"
          :disabled="award.price_in_coins > coins"
          >Collect award</CButton
        >
      </div>
    </template>
  </CModal>
</template>

<script>
import axios from "axios";
export default {
  name: "AwardDetails",
  props: {
    award: {
      type: Object,
      required: true,
    },
    modalTitle: {
      type: String,
      required: true,
    },
    coins: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      showModal: true,
      note: "",
    };
  },
  methods: {
    collectAward() {
      const token = localStorage.getItem("user-token");
      const bearer = "Bearer " + token;
      const data = {
        user: localStorage.getItem("user-id"),
        awards: this.award.id,
        user_note: this.note,
      };
      console.log(data);

      axios({
        method: "post",
        url: "https://api.motivo.localhost/collectedawards/",
        data: data,
        headers: {
          Authorization: bearer,
        },
      })
        .then((response) => {
          console.log(response);
          this.closeModal("submit");
        })
        .catch((error) => {});
    },

    closeModal(mode) {
      if (mode == "close") {
        this.$emit("closed");
      } else if (mode == "submit") {
        this.$emit("submitted");
      }
    },
  },
};
</script>

<style scoped>
</style>