<template>
  <div class="home">
    <Activities page="0" />
  </div>
</template>

<script>
// @ is an alias to /src

import Activities from '@/components/activities.vue';
import cookie from '../cookie'

export default {
  name: 'home',
  components: {
    Activities,
  },
  data(){
    return{
    }
  },
  mounted(){
    if(!cookie.getCookie('login')){
      cookie.setCookie('login', false);
    }

  }
}
</script>
<style scoped>

</style>

