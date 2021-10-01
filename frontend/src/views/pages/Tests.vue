<template>
    <div>
        <CRow>
           Tests
        </CRow>
    </div>
</template>

<script>
    import Title from './elements/Title.vue';
    import challenges from './dataTests';

    export default {
        name: 'Tests',
        components: {
            Title
        },
        data() {
            return {
                challenges: challenges,
                toDo: 3,
                failed: 5,
                passed: 6,
                counter: 65,

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