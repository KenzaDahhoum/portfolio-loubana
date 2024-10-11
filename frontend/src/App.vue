<template>
  <div id="app">
    <NavbarPage />
    <!-- Use <router-view /> to display routed components -->
    <router-view />
  </div>
</template>

<script>
import NavbarPage from './components/NavbarPage.vue';

export default {
  components: {
    NavbarPage,
  },
};
</script>

<style scoped>
/* Style for sections */
.about-section, .contact-section, #projects {
  padding-top: 100px; /* Adjust this value based on your navbar height */
  min-height: 100vh; /* Ensure each section takes up full viewport height */
}

.about-section {
  background-color: #f4f4f4;
  text-align: center;
}

.contact-section {
  background-color: #cccccc;
  text-align: center;
}

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}
</style>
