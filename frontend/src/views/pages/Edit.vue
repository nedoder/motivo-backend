<template>
  <div class="wrapper-in">
    <CWrapper>
      <TheHeader />
      <div class="formcontainer">
        <form>
          <div>
            <h4>Profile</h4>
            <hr />
          </div>
          <div class="form-group">
            <label for="exampleFormControlInput1">Name</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Name"
              v-model="editInfo.name"
              disabled
            />
          </div>
          <div class="form-group">
            <label for="exampleFormControlInput2">Surname</label>
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput2"
              placeholder="Surname"
              v-model="editInfo.surname"
              disabled
            />
          </div>
          <div class="form-group">
            <label for="exampleFormControlInput3">Email</label>
            <input
              type="email"
              class="form-control"
              id="exampleFormControlInput3"
              placeholder="Email"
              v-model="editInfo.email"
              disabled
            />
          </div>
          <div class="form-group">
            <label for="exampleFormControlInput4">Password</label>
            <input
              type="password"
              class="form-control"
              id="exampleFormControlInput4"
              placeholder="Password"
              v-model="editInfo.password"
            />
          </div>
          <div class="form-group">
            <label for="exampleFormControlInput5">Repeat password</label>
            <input
              type="password"
              class="form-control"
              id="exampleFormControlInput5"
              placeholder="Password"
              v-model="editInfo.repeat_password"
            />
          </div>

          <div class="form-group">
            <button
              type="button"
              class="btn btn-link btn-lg btn-block"
              @click="editCustom()"
              :disabled="editInfo.password != editInfo.repeat_password"
            >
              Change password
            </button>
          </div>
        </form>
      </div>
    </CWrapper>

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
import TheHeader from "../../containers/TheHeader.vue";
import axios from "axios";
import forms from "@/mixins/forms";

export default {
  name: "Edit",
  components: { TheHeader },
  data() {
    return {
      editInfo: {
        name: "",
        surname: "",
        email: "",
        password: "",
        repeat_password: "",
      },
      toastMessages: [],
    };
  },

  mixins: [forms],

  mounted() {
    this.getInitialUserData();
  },

  // @todo please use one empty line to separate elements like data, mixins, methods, mounted...
  methods: {
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

    resetPasswordForm() {
      this.editInfo.password = "";
      this.editInfo.repeat_password = "";
    },
    // @todo my version
    getInitialUserData() {
      const token = localStorage.getItem("user-token");
      const bearer = "Bearer " + token;

      axios({
        method: "get",
        url: `https://api.motivo.localhost/userdata/`,
        headers: { Authorization: bearer },
      })
        .then((res) => {
          console.log(res);
          this.editInfo.name = res.data.first_name;
          this.editInfo.surname = res.data.last_name;
          this.editInfo.email = res.data.email;
        })
        .catch((error) => console.log(error));
    },
    editCustom() {
      const data = {
        password: this.editInfo.password,
        repeat_password: this.editInfo.repeat_password,
      };

      const token = localStorage.getItem("user-token");
      const bearer = "Bearer " + token;

      axios({
        method: "put",
        url: `https://api.motivo.localhost/users/`,
        data: data,
        headers: { Authorization: bearer },
      })
        .then((resp) => {
          console.log(resp);
          // window.localStorage.clear();
          this.resetPasswordForm();
          this.addToastMessage(
            "Password changed",
            "Your password has been changed",
            "success"
          );
          // this.$router.push("/");
        })
        .catch((error) => {
          this.addToastMessage(
            "Password not changed",
            "Could not change password",
            "danger"
          );
        });
    },
  },
};
</script>

<style scoped>
form {
  width: 100%;
}

.formcontainer {
  width: 40%;
  margin: auto;
  margin-top: 8vh;
}
h4 {
  font-size: 24px;
  color: #6d7885;
  text-align: left;
  padding-bottom: 1rem;
}
a,
.btn-link {
  color: #1cb0f6;
  font-weight: bold;
  font-size: 18px;
}

input,
button {
  border-radius: 12px;
  padding: 10px;
}

button {
  color: #1cb0f6;
  font-weight: bold;
}
.wrapper-in {
  height: 100vh;
  background: #ffffff;
}
label {
  color: #99a2ad;
  font-size: 14px;
}
.btn-link {
  box-shadow: 1px 1px 3px #99a2ad;
  text-decoration: none;
}
.btn-info {
  font-weight: bold;
}

input {
  font-size: 18px;
  background: #f7f8fa;
}

#exampleFormControlInput4 {
  margin-bottom: 30px;
}
</style>