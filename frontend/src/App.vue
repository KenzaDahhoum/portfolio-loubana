<template>
  <div id="app">
    <NavbarPage />

    <!-- Home Section (corresponds to #home in the navbar) -->
    <HeaderPage id="home" />

    <!-- About Section (corresponds to #about in the navbar) -->
    <AboutSection id="about" />

    <!-- Projects Section (corresponds to #projects in the navbar) -->
    <PortfolioList id="projects" />

    <!-- Contact Section (corresponds to #contact in the navbar) -->
    <section id="contact" class="contact-section">
      <h2>Contact</h2>
      <p>Contact me through this section. Add a form or contact details here.</p>
    </section>
  </div>
</template>

<script>
import NavbarPage from './components/NavbarPage.vue';
import HeaderPage from './components/HeaderPage.vue';
import PortfolioList from './components/PortfolioList.vue';
import AboutSection from './components/AboutSection.vue'; // Import AboutSection

export default {
  components: {
    NavbarPage,
    HeaderPage,
    PortfolioList,
    AboutSection, // Register AboutSection
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
