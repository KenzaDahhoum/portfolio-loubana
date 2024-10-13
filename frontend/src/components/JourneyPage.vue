<template>
  <div class="journey-page">
    <div data-aos="fade-up">
      <EducationSection />
    </div>
    <div data-aos="fade-up">
      <ExperienceSection />
    </div>
    <div data-aos="fade-up">
      <ProjectsSection />
    </div>
    <div data-aos="fade-up">
      <SkillsSection />
    </div>
  </div>
</template>

<script>
import AOS from 'aos';
import 'aos/dist/aos.css';
import EducationSection from './EducationSection.vue';
import ExperienceSection from './ExperienceSection.vue';
import ProjectsSection from './ProjectsSection.vue';
import SkillsSection from './SkillsSection.vue';

export default {
  components: {
    EducationSection,
    ExperienceSection,
    ProjectsSection,
    SkillsSection,
  },
  mounted() {
    AOS.init({
      duration: 1000, // Animation duration
      once: true,     // Whether animation should happen only once
    });
  },
};
</script>


<style scoped>
/* General styles for the page */
.journey-page {
  padding-top: 100px;
  padding-left: 20px;
  padding-right: 20px;
  min-height: 100vh;
}

/* Center the titles */
.section h2 {
  color: #0d1330;
  font-size: 2.2rem;
  font-family: 'Pacifico', cursive;
  margin-bottom: 20px;
  text-align: center;
}

/* Card styling */
.section {
  background-color: #f9f9f9;
  margin-bottom: 20px;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
}

/* Hover effect for cards */
.section:hover {
  background-color: #eaeaea;
}
</style>
