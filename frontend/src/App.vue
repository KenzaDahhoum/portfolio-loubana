<template>
  <div id="app">
    <NavbarPage />
    <HeaderPage />
    <PortfolioList />
  </div>
</template>

<script>
import NavbarPage from './components/NavbarPage.vue';
import HeaderPage from './components/HeaderPage.vue';
import PortfolioList from './components/PortfolioList.vue';

export default {
  components: {
    NavbarPage,
    HeaderPage,
    PortfolioList,
  },
};
</script>
