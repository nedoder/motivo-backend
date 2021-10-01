<template>
  <CRow>
    <CCol col="12" xl="12">
      <CCard>
        <CCardHeader>
          UserInfo
        </CCardHeader>
        <CCardBody>
          UserInfo
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
export default {
  name: 'UserInfo',
  data () {
    return {
    }
  },
//   watch: {
//     $route: {
//       immediate: true,
//       handler (route) {
//         if (route.query && route.query.page) {
//           this.activePage = Number(route.query.page)
//         }
//       }
//     }
//   },
//   methods: {
//     getBadge (status) {
//       switch (status) {
//         case 'Active': return 'success'
//         case 'Inactive': return 'secondary'
//         case 'Pending': return 'warning'
//         case 'Banned': return 'danger'
//         default: 'primary'
//       }
//     },
//     rowClicked (item, index) {
//       this.$router.push({path: `users/${index + 1}`})
//     },
//     pageChange (val) {
//       this.$router.push({ query: { page: val }})
//     }
//   }
}
</script>
