<template>
  <div
    class="d-flex justify-content-center"
    v-bind:style="{ borderBottom: '2px solid #EBEDF0' }"
  >
    <CNavbar expandable="md" type="light" color="light" class="bg-white m-auto">
      <CToggler
        in-navbar
        @click="collapsed = !collapsed"
        class="bg-secondary"
      />
      <CHeaderNavItem
        class="nav-item mx-5"
        v-bind:style="{
          color: '#F2C94C',
          fontWeight: 'bold',
          listStyleType: 'none',
        }"
      >
        <img class="text-info" src="./motivo.png" />
      </CHeaderNavItem>
      <CCollapse :show="collapsed" navbar>
        <CNavbarNav class="ml-auto">
          <CHeaderNavItem class="px-5" v-bind:style="{ listStyleType: 'none' }">
            <CHeaderNavLink
              class="text-info"
              to="/dashboard/challenges"
              v-bind:style="{
                textDecoration: 'none',
                listStyleType: 'none',
                color: '#99A2AD !important',
              }"
            >
              <img src="./Tasks (1).png" /> Challenges
            </CHeaderNavLink>
          </CHeaderNavItem>
          <CHeaderNavItem class="px-5" v-bind:style="{ listStyleType: 'none' }">
            <CHeaderNavLink
              class="text-info"
              to="/dashboard/ranking"
              v-bind:style="{
                textDecoration: 'none',
                color: '#99A2AD  !important',
              }"
            >
              <img src="./Ranking.png" /> Ranking
            </CHeaderNavLink>
          </CHeaderNavItem>
          <CHeaderNavItem class="px-5" v-bind:style="{ listStyleType: 'none' }">
            <CHeaderNavLink
              class="text-info"
              to="/dashboard/awards"
              v-bind:style="{
                textDecoration: 'none',
                color: '#99A2AD  !important',
              }"
            >
              <img src="./Coupon.png" /> Awards
            </CHeaderNavLink>
          </CHeaderNavItem>
        </CNavbarNav>
        <!-- <CNavbarNav
      >

      </CNavbarNav> -->
        <CNavbarNav class="ml-auto">
          <CHeaderNavItem
            class="p-3"
            v-bind:style="{ color: '#F2C94C', fontWeight: 'bold' }"
          >
            <img class="text-info p-2" src="./Coin.png" />
            <template v-if="coins[0].collected_coins">{{ this.coins[0].collected_coins }}</template>
          </CHeaderNavItem>

          <CHeaderNavItem
            class="nav-item"
            v-bind:style="{
              color: '#F2C94C',
              fontWeight: 'bold',
              listStyleType: 'none',
            }"
          >
            <CDropdown placement="bottom-end" class="nth">
              <template #toggler-content>
                <img class="text-info" src="./Ellipse 23.png" />
              </template>
              <CDropdownItem v-on:click.prevent="editUser">
                <CIcon name="cil-settings" /> Settings
              </CDropdownItem>
              <CDropdownItem v-on:click.prevent="logoutCustom">
                <CIcon name="cil-lock-locked" /> Logout
              </CDropdownItem>
            </CDropdown>
          </CHeaderNavItem>
        </CNavbarNav>
      </CCollapse>
    </CNavbar>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      collapsed: false,
      coins: [],
    };
  },
  methods: {
    logoutCustom() {
      localStorage.removeItem("user-token");
      localStorage.removeItem("user-id");
      this.$router.push("/");
    },

    editUser() {
      this.$router.push("/edit");
    },

    update() {
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
          this.coins = resp.data.results;
          let userid = parseInt(localStorage.getItem("user-id"));
          this.coins = this.coins.filter((result) => result.id === userid);
        })
        .catch((error) => console.log(error));
    },
  },

  /**
   * 
   */
  mounted() {
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
        this.coins = resp.data.results;
        let userid = parseInt(localStorage.getItem("user-id")); 
        this.coins = this.coins.filter((result) => result.id === userid);
        console.log("Coins: ", this.coins);
      })
      .catch((error) => console.log(error));

    window.addEventListener("click", (event) => {
      this.update();
    });
  },
};
</script>