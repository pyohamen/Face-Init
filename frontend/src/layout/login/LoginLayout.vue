<template>
  <div class="wrapper">
    <div class="main-panel">
      <login-content>

      </login-content>
    </div>
  </div>
</template>
<style lang="scss">
</style>
<script>
/* eslint-disable */
  import LoginContent from "./Content.vue"
  import MobileMenu from "./MobileMenu"
  export default {
    components: {
      LoginContent,
      MobileMenu
    },
    mounted() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    }
  };
</script>
