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
      <ContactForm />
    </section>
  </div>
</template>

<script>
import HeaderPage from './HeaderPage.vue';
import AboutSection from './AboutSection.vue';
import PortfolioList from './PortfolioList.vue';
import ContactForm from './ContactForm.vue';

export default {
components: {
  HeaderPage,
  AboutSection,
  PortfolioList,
  ContactForm,
},
};
</script>

<style scoped>
/* Style for sections */

/* Home Section */
#home {
color: white;
}

/* About Section */
.about-section {
background-color: #d4dce3; 
padding-top: 100px;
min-height: 100vh;
text-align: center;
}

/* Loubana Skincare Section */
#projects {
background-color: #f5f0e8; 
padding-top: 100px;
min-height: 100vh;
text-align: center;
}
</style>
