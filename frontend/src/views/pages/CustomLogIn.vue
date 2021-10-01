<template>
  <div class="wrapper-in">
    <div class="motivo">
      <img src="./img/motivo.png" />
      <div class="formcontainer">
        <form>
          <div>
            <h4>Sign in</h4>
          </div>
          <div class="form-group">
            <label for="exampleFormControlInput1">Email</label>
            <input
              type="email"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="Email"
              v-model="loginInfo.email"
            />
          </div>
          <div class="form-group">
            <label for="exampleFormControlInput2">Password</label>
            <input
              type="password"
              class="form-control"
              id="exampleFormControlInput2"
              placeholder="Password"
              v-model="loginInfo.password"
            />
          </div>
          <div class="form-group">
            <a href="#">Forgot password</a>
          </div>
          <div class="form-group">
            <button
              type="button"
              class="btn btn-info btn-lg btn-block"
              v-on:click.prevent="loginCustom"
            >
              Login
            </button>
          </div>
          <div class="form-group">
            <button type="button" class="btn btn-link btn-lg btn-block">
              I don't have an account
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.headers.get["Content-Type"] =
  "application/x-www-form-urlencoded";
axios.defaults.headers.post["Content-Type"] = "multipart/form-data";
import { postRequest } from "@/utils/http";
import forms from "@/mixins/forms";

export default {
  name: "CustomLogIn",
  data() {
    return {
      loginInfo: {
        email: "",
        password: "",
        token: localStorage.getItem("user-token") || null,
      },
    };
  },

  mixins: [forms],

  // @todo please use one empty line to separate elements like data, mixins, methods, mounted...
  methods: {
    // @todo my version
    login() {
      const data = {
        username: this.loginInfo.email,
        password: this.loginInfo.password,
      };
    },

    /**
     * Send email and password to authenticate user.
     * Returns access and refresh token.
     */
    loginCustom() {
      const data = {
        email: this.loginInfo.email,
        password: this.loginInfo.password,
      };
      axios({
        method: "post",
        url: "https://api.motivo.localhost/api/token/",
        data: data,
      })
        .then((resp) => {
          this.token = resp.data.access;
          localStorage.setItem("user-token", resp.data.access);
          localStorage.setItem("user-refresh", resp.data.refresh);

          const token = localStorage.getItem("user-token");
          const bearer = "Bearer " + token;

          axios({
            method: "get",
            url: "https://api.motivo.localhost/userdata/",
            headers: {
              Authorization: bearer,
            },
          })
            .then((resp) => {
              localStorage.setItem('user-id', resp.data.id)
            })
            .catch((err) => {
              console.log(err);
            })
            .finally(() => {
              this.$router.push("/dashboard/challenges/");
            });
        })
        .catch((error) => console.log(error));
    },
  },

  mounted() {
    window.addEventListener("keyup", (event) => {
      if (event.keyCode === 13) {
        console.log("Captured: ", event.key)
        this.loginCustom();
      }
    });
  },
};
</script>

<style scoped>
.wrapper-in {
  background: #ffffff;
  height: 100vh;
}

form {
  width: 100%;
}

.formcontainer {
  width: 40%;
  margin: auto;
  margin-top: 10%;
}

.motivo {
  width: 100%;
  margin: auto;
  padding: 30px 50px;
}

h4 {
  text-align: center;
  padding-bottom: 1rem;
  font-size: 24px;
  color: #6d7885;
}

a,
.btn-link {
  color: #1cb0f6;
  font-weight: bold;
  font-size: 18px;
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

input,
button {
  border-radius: 12px;
  padding: 10px;
}

input {
  font-size: 18px;
  background: #f7f8fa;
}
</style>