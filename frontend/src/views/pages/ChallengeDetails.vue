<template>
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
  },
  //   beforeRouteEnter(to, from, next) {
  //     next((vm) => {
  //       vm.challengesOpened = from.fullPath.includes("challenges");
  //     });
  //   },
  data() {
    return {
      usersOpened: null,
      tasks: null,
      description: "",
      file: "",
    };
  },
  filters: {
    capitalize: function (value) {
      if (!value) return "";
      value = value.toString();
      return value.toUpperCase();
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