<template>
  <div class="wrapper main-custom">
    <side-bar title="Face Init">
      <template slot="links">
        <sidebar-link to="/home" :name="$t('Home')" icon="tim-icons icon-chart-pie-36"/>
        <sidebar-link to="/management" :name="$t('Management')" icon="tim-icons icon-settings-gear-63"/>
      </template>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content @click.native="toggleSidebar">

      </dashboard-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss">
</style>
<script>
/* eslint-disable */
  import TopNavbar from "./MainNavbar.vue";
  import ContentFooter from "./MainFooter.vue";
  import DashboardContent from "./Content.vue";
  import MobileMenu from "./MobileMenu";
  export default {
    components: {
      TopNavbar,
      ContentFooter,
      DashboardContent,
      MobileMenu
    },
    methods: {
      toggleSidebar() {
        if (this.$sidebar.showSidebar) {
          this.$sidebar.displaySidebar(false);
        }
      }
    }
  };
</script>
<style>
@font-face {
  font-family: "my-icons";
  src: url('../../assets/fonts/NanumSquareRoundB.ttf') format('truetype'),;
}

.main-custom{
}
</style>
