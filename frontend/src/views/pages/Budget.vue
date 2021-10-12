<template>
  <div>
    <CRow class="mb-5">
      <CCol class="col-3" v-for="(section, index) in sections">
        <div class="category_card">
          <h3 class="text-center">
            {{ section.name }}:
            <span class="card_amount">{{ section.value }}</span>
          </h3>
        </div>
      </CCol>

      <CCol class="col-3">
        <div @click="addNewPosition()" class="card_hoverable">
          <h3 class="text-center">
            Add new position <br />
            <span>
              <font-awesome-icon icon="plus" />
            </span>
          </h3>
        </div>
      </CCol>
    </CRow>

    <CDataTable
      v-bind:style="{
        borderRadius: '18px',
        border: '2px solid #EBEDF0',
        padding: '10px',
        margin: '10px',
      }"
      :items="budgetData"
      :fields="table_headers"
      :items-per-page="20"
      :header="true"
      :pagination="{ doubleArrows: false, align: 'center' }"
    >
    </CDataTable>

    <add-budget-position-modal
      v-if="showModal"
      @closed="showModal = false"
      @submitted="onBudgetPositionSubmitted()"
    ></add-budget-position-modal>

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
import AddBudgetPositionModal from "./AddBudgetPositionModal.vue";

export default {
  components: {
    AddBudgetPositionModal,
  },
  data() {
    return {
      showModal: false,
      annual_personal_budget_amount: 0,
      budget_left: 0,
      days_left_to_burn_budget: 0,
      sections: [],
      budgetData: [],
      toastMessages: [],
      table_headers: [
        {
          key: "title",
          label: "Title",
        },
        {
          key: "category",
          label: "Category",
        },
        {
          key: "when",
          label: "When",
        },
        {
          key: "amount",
          label: "Amount",
        },
        {
          key: "comment",
          label: "Comment",
        },
        {
          key: "file",
          label: "File",
        },
        {
          key: "status",
          label: "Status",
        },
      ],
    };
  },

  mounted() {
    this.getListOfBudgets();
  },

  methods: {
    addNewPosition() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
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
    onBudgetPositionSubmitted() {
      this.closeModal();
      this.addToastMessage(
        "Position added",
        "A budget table was successfully updated",
        "success"
      );

      // Download challenge data again
      this.getListOfBudgets();
    },
    getListOfBudgets() {
      const token = localStorage.getItem("user-token");
      const bearer = "Bearer " + token;

      const budget = axios({
        method: "get",
        url: "https://api.motivo.localhost/budget/management/",
        headers: {
          Authorization: bearer,
        },
      });

      Promise.all([budget])
        .then(([budgetResponse]) => {
          console.log(budgetResponse);

          // Get the budget responses and save them in data storage
          this.budgetData = budgetResponse.data.budgets_table_data;
          this.annual_personal_budget_amount =
            budgetResponse.data.annual_personal_budget_amount;
          this.budget_left = budgetResponse.data.budget_left;
          this.days_left_to_burn_budget =
            budgetResponse.data.days_left_to_burn_budget;

          // Prepare proper sections with names and values to be displayed
          var sections = [
            { name: "Budget left gross", value: this.budget_left },
            {
              name: "Annual personal budget amount gross",
              value: this.annual_personal_budget_amount,
            },
            {
              name: "Days left to burn budget",
              value: this.days_left_to_burn_budget,
            },
          ];

          // Assign the sections to local data
          this.sections = sections;
        })
        .catch((error) => console.log(error));
    },
  },
  pageChange() {
    return;
  },
};
</script>

<style scoped>
.category_card {
  border: 2px solid #ebedf0;
  box-shadow: 0px 2px 0px #cfd8da;
  border-radius: 18px;
  height: 200px;
  width: 23vw;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  box-shadow: -2px 4px 1px #c3c3c3ad;
}

.card_hoverable {
  /* border: 2px solid #ebedf0; */
  box-shadow: 0px 2px 0px rgba(52, 152, 52, 0.756);
  border-radius: 18px;
  height: 200px;
  width: 23vw;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  box-shadow: -2px 4px 1px #c3c3c3ad;

  background-color: rgb(68, 162, 68);
  color: white;
}

.card_hoverable:hover {
  transform: translateY(5px);
  box-shadow: 0px 0px 3px #c3c3c3ad;
  cursor: pointer;
}

tbody > tr {
  background-color: white !important;
}

.card_amount {
  position: absolute;
  bottom: 3vh;
  left: 40%;
  /* color: rgb(82, 192, 211); */
}
</style>