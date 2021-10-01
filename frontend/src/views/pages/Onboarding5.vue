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
          <img src="./img/blog(2).png" class="img-fluid" alt="Responsive image" />
        </div>
        <div class="text">
          <p>Take part at friendly competition</p>
          <h4>Check the ranking list and follow the progress of other participants</h4>
        </div>
      </CContainer>
      <div class="container links">
        <img src="./img/Group 240(4).png" />
        <CLink to="/dashboard/tasks" class="link two">Finish ></CLink>
      </div>
    </CWrapper>
  </div>
</template>

<script>
  export default {
    name: 'Onboarding5',
  }
</script>

<style scoped>
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
    width: 40%;
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
    padding: 0;
    margin-bottom: 20px;
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