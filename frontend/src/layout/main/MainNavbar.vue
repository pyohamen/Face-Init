<template>
  <nav class="navbar navbar-expand-lg navbar-absolute"
       :class="{'bg-white': showMenu, 'navbar-transparent': !showMenu}">
    <div class="container-fluid" style="height:46px">
      <div class="navbar-wrapper">
        <div class="navbar-toggle d-inline" :class="{toggled: $sidebar.showSidebar}">
          <button type="button" class="navbar-toggler"
                  @click="toggleSidebar">
            <span class="navbar-toggler-bar bar1"></span>
            <span class="navbar-toggler-bar bar2"></span>
            <span class="navbar-toggler-bar bar3"></span>
          </button>
        </div>
        <label class="navbar-brand">{{routeName}}</label>
      </div>

      <collapse-transition>
        <div class="show">
          <ul class="navbar-nav" :class="$rtl.isRTL ? 'mr-auto' : 'ml-auto'">
            <base-button size="sm" class="animation-on-hover" type="default" @click.prevent="onClickLogout">로그 아웃</base-button>
          </ul>
        </div>
      </collapse-transition>
    </div>
  </nav>
</template>
<script>
/* eslint-disable */
  import { CollapseTransition } from 'vue2-transitions';
  import Modal from '@/components/Modal';
  import store from '@/store'

  export default {
    components: {
      CollapseTransition,
      Modal
    },
    computed: {
      routeName() {
        const { name } = this.$route;
        return this.capitalizeFirstLetter(name);
      },
      isRTL() {
        return this.$rtl.isRTL;
      }
    },
    data() {
      return {
        activeNotifications: false,
        showMenu: false,
        searchModalVisible: false,
        searchQuery: ''
      };
    },
    methods: {
      onClickLogout () {
        store.dispatch('LOGOUT').then(() => this.$router.push('/login'))
      },
      capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
      },
      toggleNotificationDropDown() {
        this.activeNotifications = !this.activeNotifications;
      },
      closeDropDown() {
        this.activeNotifications = false;
      },
      toggleSidebar() {
        this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
      },
      hideSidebar() {
        this.$sidebar.displaySidebar(false);
      },
      toggleMenu() {
        this.showMenu = !this.showMenu;
      }
    }
  };
</script>
<style>
</style>
