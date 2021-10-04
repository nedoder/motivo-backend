<template>
  <!-- Modal with the challenge details -->
  <CModal
    :title="modalTitle"
    color="info"
    :centered="true"
    size="lg"
    :show.sync="showModal"
  >
    <div class="p-4">
      <!-- Coins image -->
      <CRow class="my-1">
        <p class="coin_text">
          {{ challenge.coins_to_win }} &nbsp;
          <img class="text-info" src="./img/Coin.png" />
        </p>
      </CRow>

      <!-- Challenge image -->
      <CRow
        class="m-auto"
        v-bind:style="{
          display: 'flex',
          position: 'relative',
          width: '120px',
          height: '135px',
          clipPath:
            'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)',
        }"
      >
        <img
          v-bind:src="challenge.image"
          alt="Award image"
          v-bind:style="{
            width: '100%',
            height: 'auto',
            display: 'block',
            objectFit: 'cover',
          }"
        />
      </CRow>

      <!-- Challenge title -->
      <CRow class="my-1">
        <h2>{{ challenge.title | capitalize }}</h2>
      </CRow>

      <!-- Challenge description -->
      <CRow class="my-1">
        <p class="px-3" v-linkified :style="[{ textAlign: 'justify' }]">
          {{ challenge.description }}
        </p>
      </CRow>

      <!-- Challenge comment -->
      <CRow class="my-1">
        <CTextarea
          label="Your comment"
          class="w-100"
          v-model="description"
          placeholder="Tell us how did you complete the challenge :)"
          required
        />
      </CRow>

      <!-- File to be attached by the user -->
      <CRow class="my-1">
        <p>Attach file</p>
      </CRow>
      <CRow class="my-1">
        <input
          type="file"
          id="file"
          ref="file"
          v-on:change="handleFileUpload()"
        />
      </CRow>
    </div>
    <!-- Overwritten footer style -->
    <template #footer>
      <div class="w-100 d-flex justify-content-between">
        <CButton @click="closeModal('close')" color="danger">Cancel</CButton>
        <CButton @click="uploadAttempt()" color="success">Submit</CButton>
      </div>
    </template>

    <!-- Toast message to be displayed -->
    <!-- <CToaster :autohide="3000">
      <template v-for="toastMessage in toastMessages">
        <CToast
          :key="toastMessage.id"
          :show="true"
          :header="toastMessage.header"
        >
          {{ toastMessage.content }}
        </CToast>
      </template>
    </CToaster> -->
  </CModal>
</template>

<script>
import axios from "axios";
export default {
  name: "ChallengeDetails",
  props: {
    challenge: {
      type: Object,
      required: true,
    },
    modalTitle: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      usersOpened: null,
      tasks: null,
      description: "",
      file: "",
      showModal: true,
    };
  },
  filters: {
    capitalize: function (value) {
      if (!value) return "";
      value = value.toString();
      return value.toUpperCase();
    },
  },
  methods: {
    closeModal(mode) {
      if (mode == "close") {
        this.$emit("closed");
      } else if (mode == "submit") {
        this.$emit("submitted");
      }
    },

    handleFileUpload() {
      this.file = this.$refs.file.files[0];
      console.log(this.file);
    },

    uploadAttempt() {
      const token = localStorage.getItem("user-token");
      const bearer = "Bearer " + token;

      let formData = new FormData();
      formData.append("file", this.file);
      formData.append("user", localStorage.getItem("user-id"));
      formData.append("challenge", this.challenge.id);
      formData.append("description", this.challenge.description);

      axios({
        method: "post",
        url: "https://api.motivo.localhost/attempt/",
        data: formData,
        headers: {
          Authorization: bearer,
          "Content-Type": "multipart/form-data",
        },
      })
        .then((response) => {
          console.log(response);
          this.closeModal('submit');
        })
        .catch((error) => {
          this.addToastMessage(
            "Error",
            "Something went wrong - your attempt could not be completed.",
            "danger"
          );
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.bordered {
  border-radius: 18px;
  border: 2px solid #ebedf0;
}
</style>