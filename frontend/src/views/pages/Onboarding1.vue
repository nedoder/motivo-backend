<template>
  <div class="c-app bg-white">
    <CWrapper>
      <div class="container logo">
        <img src="./img/motivo.png" />
      </div>
      <CContainer class='bg-white'>
        <div class="container">
          <CLink to="/dashboard/challenges" class="link">Skip</CLink>
        </div>
        <div class="motivo">
          <img src="./img/image.png" class="img-fluid" alt="Responsive image" />
        </div>
        <div class="text">
          <p>Manage tasks easily</p>
          <h4>To change status of task just simply hold & drag it left or right</h4>
        </div>
      </CContainer>
      <div class="container links">
        <img src="./img/Group 240.png" />
        <CLink to="/onboarding2" class="link two">Next ></CLink>
      </div>
    </CWrapper>
  </div>
</template>

<script>
  export default {
    name: 'Onboarding1',
    mounted() {
      const token = localStorage.getItem('user-token')
      const bearer = 'Bearer ' + token
      axios({
          method: 'get',
          url: 'https://api.motivo.localhost/userdata/',
          headers: {
            'Authorization': bearer,
          }
        })
        .then(resp => {
          localStorage.setItem('user-id', resp.data.results[0].id)
          localStorage.setItem('user-name', resp.data.results[0].first_name)
          localStorage.setItem('user-surname', resp.data.results[0].last_name)
          localStorage.setItem('user-email', resp.data.results[0].email)
        })
        .catch(error => console.log(error))
    },
  }
</script>

<style scoped>
  .wrapper-div {
    height: 100vh;
    background: #ffffff;
  }

  .logo {
    width: 80%;
    padding: 30px;
  }

  .motivo {
    width: 80%;
    margin: auto;
    display: flex;
  }

  .motivo img {
    margin: auto;
  }

  .link {
    float: right;
    color: #D3D9DE;
    font-weight: bold;
    text-decoration: none;
  }

  .two {
    color: #1CB0F6;
  }

  .links {
    margin-bottom: 5px;
  }

  .text {
    width: 60%;
    font-size: 18px;
    margin: 20px auto;
    text-align: left;
    color: #99A2AD;
    font-weight: bold;
  }

  h4 {
    font-size: 36px;
    color: #2C2D2E;
  }
</style>