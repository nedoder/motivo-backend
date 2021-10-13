<template>
  <!-- Modal with the challenge details -->
  <CModal
    title="Add new budget position"
    color="info"
    :centered="true"
    size="lg"
    :show.sync="showModal"
  >
    <template #header> <h5 class="pt-1">Add new budget position</h5> </template>

    <div class="p-3">
      <!-- Title input -->
      <CRow class="my-1">
        <CInput
          v-model="formData.title"
          type="text"
          class="w-100"
          placeholder="Insert the title"
          label="Title"
        ></CInput>
      </CRow>

      <!-- Category select -->
      <CRow class="my-1">
        <CSelect
          label="Select Category"
          class="w-100"
          :options="selectCategoryOptions"
          :value.sync="formData.category"
          placeholder="Select category"
        />
      </CRow>

      <!-- When -->
      <CRow class="my-1">
        <CInput
          type="date"
          class="w-100"
          label="When"
          v-model="formData.when"
        ></CInput>
      </CRow>

      <!-- Amount in PLN -->
      <CRow class="mt-3 mb-1">
        <CInput
          v-model="formData.amount"
          class="w-100"
          label="Amount (PLN)"
          type="number"
          min="0"
          placeholder="0 PLN"
          :value="0"
        >
        </CInput>
      </CRow>

      <!-- Comment -->
      <CRow class="my-1">
        <CTextarea
          v-model="formData.comment"
          class="w-100"
          label="Comment"
          type="number"
          placeholder="Put your comment here"
        >
        </CTextarea>
      </CRow>

      <!-- File to be uploaded -->
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
        <CButton @click="onSubmit()" color="success">Submit</CButton>
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
import Datepicker from "vuejs-datepicker";

export default {
  name: "AddBudgetPositionModal",
  props: {},
  components: {
    Datepicker,
  },
  data() {
    return {
      api_url: process.env.VUE_APP_API_URL,
      showModal: true,
      formData: {
        title: "",
        category: "",
        when: "",
        amount: 0,
        comment: "",
      },
      file: null,
      selectCategoryOptions: [],
    };
  },
  mounted() {
    this.getAllCategories();
  },
  methods: {
    /**
     * Get all the available budget categories from the server
     */
    getAllCategories() {
      const token = localStorage.getItem("user-token");
      const bearer = "Bearer " + token;
      axios({
        method: "get",
        url: `${this.api_url}/budget/categories/`,
        headers: {
          Authorization: bearer,
        },
      })
        .then((resp) => {
          this.selectCategoryOptions = resp.data;
        })
        .catch((error) => console.log(error));
    },
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

    onSubmit() {
      const token = localStorage.getItem("user-token");
      const bearer = "Bearer " + token;

      let formData = new FormData();
      formData.append("file", this.file);
      formData.append("budget_data", JSON.stringify(this.formData));

      axios({
        method: "post",
        url: `${this.api_url}/budget/management/`,
        data: formData,
        headers: {
          Authorization: bearer,
          "Content-Type": "multipart/form-data",
        },
      })
        .then((response) => {
          console.log(response);
          this.closeModal("submit");
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