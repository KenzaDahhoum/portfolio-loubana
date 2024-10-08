<template>
  <div id="app">
    <PortfolioList />
  </div>
</template>

<script>
import PortfolioList from './components/PortfolioList.vue';

export default {
  components: {
    PortfolioList
  }
}
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
