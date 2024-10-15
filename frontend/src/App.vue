<template>
  <div id="app">
    <NavbarPage />
    <!-- Use <router-view /> to display routed components -->
    <router-view />
    <FooterPage />
  </div>
</template>

<script>
import NavbarPage from './components/NavbarPage.vue';
import FooterPage from './components/FooterPage.vue';

export default {
  components: {
    NavbarPage,
    FooterPage,
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

html, body, #app {
  margin: 0;
  padding: 0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

#app {
  flex: 1;
}

.router-view {
  flex: 1;
}

footer {
  background-color: #0d1330;
  color: #fff;
  text-align: center;
  padding: 20px;
  margin-top: auto;
}

footer .social-links a {
  color: #ffd600;
  margin: 0 10px;
  font-size: 1.5rem;
}

footer .social-links a:hover {
  color: #fff;
}

.about-section, .loubana-section, .contact-section {
  padding-top: 100px;
  min-height: 100vh;
}

.loubana-section {
  background-color: #f4f4f4;
  padding-bottom: 60px; /* Increase space before Contact */
}

.contact-section {
  background-color: #cccccc;
  padding-top: 60px; /* Adjust space after Loubana */
  padding-bottom: 60px;
}
</style>