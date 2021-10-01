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
          <img src="./img/blog(1).png" class="img-fluid" alt="Responsive image" />
        </div>
        <div class="text">
          <p>Check your knowledge</p>
          <h4>Solve tests for check your knowledge about the company processes and remember that bigger score means more
            points!</h4>
        </div>
      </CContainer>
      <div class="container links">
        <img src="./img/Group 240(3).png" />
        <CLink to="/onboarding5" class="link two">Next ></CLink>
      </div>

    </CWrapper>
  </div>
</template>

<script>
  export default {
    name: 'Onboarding4',
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