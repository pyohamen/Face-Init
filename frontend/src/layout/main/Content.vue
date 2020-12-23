<template>
  <div class="content">
    <fade-transition :duration="100" mode="out-in">
      <!-- your content here -->
      <router-view></router-view>
    </fade-transition>
  </div>
</template>
<script>
/* eslint-disable */
  import {FadeTransition} from 'vue2-transitions';
  export default {
    components: {
      FadeTransition
    }
  };
</script>
