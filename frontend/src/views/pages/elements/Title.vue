<template>
    
        <CCard bodyWrapper :style="{color: activeColor}">
            <CRow>
                <CCol sm="8">
                    {{text}}
                </CCol>
                <CCol sm="4">
                    {{number}}
                </CCol>
            </CRow>
        </CCard>
    
</template>

<script>
    export default {
        name: 'Title',
        props: {
            activeColor: String,
            text: String,
            number: Number
        }
    }
</script>

<style>

</style>