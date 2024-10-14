<template>
  <div class="journey-page">
    <!-- Education Section -->
    <div data-aos="fade-up" data-aos-duration="1000">
      <EducationSection />
    </div>
    <!-- Experience Section -->
    <div data-aos="fade-up" data-aos-duration="1000" data-aos-delay="200">
      <ExperienceSection />
    </div>
    <!-- Projects Section -->
    <div data-aos="fade-up" data-aos-duration="1000" data-aos-delay="400">
      <ProjectsSection />
    </div>
    <!-- Skills Section -->
    <div data-aos="fade-up" data-aos-duration="1000" data-aos-delay="600">
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
      duration: 1000, // General animation duration
      once: true, // Animation happens only once
      easing: 'ease-in-out',
    });
  },
};
</script>

<style scoped>
.journey-page {
  padding: 100px 20px;
  min-height: 100vh;
}

.section {
  background-color: #f9f9f9;
  margin-bottom: 20px;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}


.section:hover {
  background-color: #eaeaea;
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.2);
}

h2 {
  font-size: 2.4rem;
  font-family: 'Pacifico', cursive;
  text-align: center;
  color: #0d1330;
  margin-bottom: 20px;
}
</style>
