<template>
  <div class="personal">
    <Activities :page="page" />
  </div>
</template>
<script>

import Activities from '@/components/activities.vue'

export default {
  name: 'personal',
  components: {
    Activities,
  },
  data(){
    return{
      page: 'post'
    }
  },
  mounted(){
    this.page = this.$route.params.page;
  }
}
</script>
<style scoped>

</style>
