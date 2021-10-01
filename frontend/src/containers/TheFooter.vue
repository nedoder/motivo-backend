<template>
  <CFooter :fixed="false">
    <div class='left-side'>
      <a href="https://vstorm.co/" target="_blank">
      &copy; {{new Date().getFullYear()}} VSTORM All right reserved.
      </a>
    </div>
    <div class="mfs-auto right-side">
      <CIcon name="cib-linkedin"/><a href="https://www.linkedin.com/company/vstormco/"></a>
      <CIcon name="cib-facebook"/><a href="https://www.facebook.com/vstormco/"></a>
      <CIcon name="cib-dribbble"/><a href="https://dribbble.com/vstorm"></a>
    </div>
  </CFooter>
</template>

<script>
export default {
  name: 'TheFooter'
}
</script>


<style scoped>
  .left-side a {
    color: #1CB0F6;
    text-decoration: none;
    font-weight: bold;
  }
  .right-side a {
    padding-right: 20px;
  }
</style>