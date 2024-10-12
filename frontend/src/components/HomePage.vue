<!-- src/components/MainPage.vue -->
<template>
    <div>
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
  import HeaderPage from './HeaderPage.vue';
  import AboutSection from './AboutSection.vue';
  import PortfolioList from './PortfolioList.vue';
  
  export default {
    components: {
      HeaderPage,
      AboutSection,
      PortfolioList,
    },
  };
  </script>
  
  <style scoped>
  /* Style for sections */
  .about-section, .contact-section, #projects {
    padding-top: 100px;
    min-height: 100vh;
  }
  
  .about-section {
    background-color: #f4f4f4;
    text-align: center;
  }
  
  .contact-section {
    background-color: #cccccc;
    text-align: center;
  }
  </style>
  