// @oliwia: I commented the imports that were not working

//import FormAlerts from '@/components/FormAlerts.vue';
//import FormMessages from '@/components/FormMessages.vue';
//import { checkRequired } from '@/utils/validation';
import forIn from 'lodash-es/forIn';
import {
  ValidationProvider, ValidationObserver, setInteractionMode, localize,
} from 'vee-validate';
import en from 'vee-validate/dist/locale/en.json';

setInteractionMode('lazy');
localize({ en });

export default {
  data() {
    return {
      invalidMsg: [],
      formMsg: [],
      loading: false,
      errorTabs: [],
      uploadHeaders: {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRF-TOKEN': window.csrfToken,
        Accept: 'application/json',
        'X-Socket-Id': window.Echo ? window.Echo.socketId() : null,
      },
    };
  },

  components: {
    //FormAlerts,
    //FormMessages,
    ValidationProvider,
    ValidationObserver,
  },

  methods: {
    //checkRequired: (rules) => checkRequired(rules),

    handleForm(formName) {
      this.loading = true;
      this.invalidMsg = [];
      this.formMsg = [];
      this.submitForm()
        .then(() => {
        })
        .catch((error) => {
          console.log({ error });
          this.$refs[formName].reset();

          if (error.status === 422) { // validation error
            // eslint-disable-next-line prefer-const
            let serverSideErrors = {};
            forIn(error.data.errors, (err, field) => {
              let errorItem = err;
              if (!Array.isArray(errorItem)) {
                errorItem = [errorItem];
              }
              this.invalidMsg.push(errorItem[0]);
              serverSideErrors[field] = [errorItem[0]];
            });
            this.$refs[formName].setErrors(serverSideErrors);
          }
        })
        .finally(() => {
          this.loading = false;
        });
    },

    clearInvalidMsg() {
      this.invalidMsg = [];
    },
  },
};
