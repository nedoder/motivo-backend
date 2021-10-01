/* eslint-disable no-undef */
import axios from 'axios';

const api = axios.create({
  withCredentials: true,
  baseURL: process.env.VUE_APP_API_URL,
  timeout: 50000,
  headers: {
    'X-Requested-With': 'XMLHttpRequest',
    Accept: 'application/json',
  },
});

api.interceptors.response.use(
  (response) => {
    // Any status code that lie within the range of 2xx cause this function to trigger
    // Do something with response data
    if (response.data.message) {
      // vm.$notifySuccess(response.data.message);
    }

    return response;
  },
  (error) => {
    if (typeof error !== 'object' || !('response' in error)) {
      return;
    }
    if (error.response) {
      if (error.response.status === 429) {
        vm.$notifyError('Too Many Attempts.'); // wyskakujace powiadomienia z coreUI
      }

      if (error.response.status === 403) {
        console.error(`403: ${error.request.responseURL}`);
        vm.$notifyError('You don\'t have right to this resource!');
      }

      if (error.response.status === 401) { // Unauthorized error
        console.error(`401: ${error.request.responseURL}`);
        window.sessionStorage.setItem('intended', vm.$router.currentRoute.fullPath);
        vm.$router.push({ name: 'auth.login' });
      }

      // CSRF Token error, repeat last request
      if (error.response.status === 419) {
        // eslint-disable-next-line consistent-return
        return api.get('/sanctum/csrf-cookie')
          .then(() => axios(error.response.config))
          .catch((tokenError) => {
            console.error({ tokenError });
            return Promise.reject(tokenError);
          });
      }

      // this fragment should be last
      // if (error.response.status !== 422) {
      //   const msg = error.response.data.message || error.message;
      //   this.$message.error(msg);
      // }
    } else if (error.request) {
      console.log({ 'Request error': error.request });
    } else {
      console.log('Error', error.message);
    }

    console.log('rejected');
    // eslint-disable-next-line consistent-return
    return Promise.reject(error);
  },
);

export const esc = encodeURIComponent;

export function qs(params) {
  return Object.keys(params)
    .map((k) => `${esc(k)}=${esc(params[k])}`)
    .join('&');
}

export function postRequest(uri, data = {}) {
  return new Promise((resolve, reject) => {
    api
      .post(uri, data)
      .then((response) => {
        resolve(response.data);
      })
      .catch((errors) => {
        console.log({ errors });
        reject(errors.response);
      });
  });
}

export function postMultipartRequest(uri, formData) {
  return new Promise((resolve, reject) => {
    api.post(uri, formData)
      .then((response) => {
        // checkResponse(response)
        resolve(response.data);
      })
      .catch((errors) => {
        // checkError(errors)

        if ('response' in errors) {
          reject(errors.response);
        }
        if ('error' in errors) {
          reject(errors.error);
        }
      });
  });
}

export function putRequest(uri, data = {}) {
  return new Promise((resolve, reject) => {
    api
      .put(uri, data)
      .then((response) => {
        resolve(response.data);
      })
      .catch((errors) => {
        reject(errors.response);
      });
  });
}

export function patchRequest(uri, data = {}) {
  return new Promise((resolve, reject) => {
    api
      .patch(uri, data)
      .then((response) => {
        resolve(response.data);
      })
      .catch((errors) => {
        reject(errors.response);
      });
  });
}

export function deleteRequest(uri, data = {}) {
  return new Promise((resolve, reject) => {
    api
      .delete(uri, data)
      .then((response) => {
        resolve(response.data);
      })
      .catch((errors) => {
        reject(errors.response);
      });
  });
}

export function getRequest(url, data = {}) {
  let uri = url;
  if (Object.keys(data).length > 0) {
    uri = `${uri}?${qs(data)}`;
  }

  return new Promise((resolve, reject) => {
    api
      .get(uri)
      .then((response) => {
        resolve(response.data);
      })
      .catch((errors) => {
        reject(errors.response);
      });
  });
}

export function downloadRequest(url, filename, data = {}) {
  let uri = url;
  if (Object.keys(data).length > 0) {
    uri = `${uri}?${qs(data)}`;
  }

  return new Promise((resolve, reject) => {
    api
      .get(uri, {
        responseType: 'blob',
        headers: {},
      })
      .then((response) => {
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(new Blob([response.data]));
        link.setAttribute('download', filename);
        document.body.appendChild(link);
        link.click();
      })
      .catch((errors) => {
        reject(errors.response);
      });
  });
}

export function uploadRequest(uri, data) {
  return fetch(uri, {
    headers: {},
    cors: true,
    method: 'POST',
    body: data,
  });
}

export default api;
