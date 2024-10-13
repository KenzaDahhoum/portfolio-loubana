<template>
    <div class="projects-section section">
      <h2>Projects</h2>
      <div 
        class="project-card" 
        v-for="project in projects" 
        :key="project.id"
        data-aos="flip-left"  
        data-aos-duration="1000" 
      >
        <strong class="title">{{ project.shortTitle }}</strong>
        <p class="description">{{ project.description }}</p>
        <p class="technologies">Technologies used: <span>{{ project.technologies }}</span></p>
      </div>
    </div>
</template>

<script>
import axios from 'axios';
import AOS from 'aos';  // Importing AOS for animation
import 'aos/dist/aos.css';  // Importing AOS CSS

export default {
  data() {
    return {
      projects: []
    };
  },
  mounted() {
    this.fetchProjects();
    AOS.init();  // Initialize AOS on mounted
  },
  updated() {
    AOS.refresh();  // Refresh AOS when content updates
  },
  methods: {
    async fetchProjects() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/projects');
        this.projects = response.data.map(project => {
          return {
            ...project,
            shortTitle: this.getShortTitle(project.title),
          };
        });
      } catch (error) {
        console.error("Error fetching projects data", error);
      }
    },
    getShortTitle(title) {
      const titlesMap = {
        "HRZen Management System": "HRZen System",
        "Frontend for Real Estate Platform": "Real Estate Platform",
        "Chichaoua Web Development Project": "Chichaoua Project",
        "DIGISBAI Web Development": "DIGISBAI Development",
      };
      return titlesMap[title] || title;
    }
  }
};
</script>

<style scoped>
.section h2 {
  color: #0d1330;
  font-size: 2.2rem;
  font-family: 'Pacifico', cursive;
  text-align: center;
  margin-bottom: 20px;
}

.projects-section {
  margin-bottom: 2rem;
}

.project-card {
  margin-bottom: 1.5rem;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
}

.project-card .title {
  font-size: 1.4rem;
  color: #ffd600;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.project-card .description {
  font-size: 1.1rem;
  margin-bottom: 0.3rem;
}

.project-card .technologies {
  font-size: 1rem;
  color: #888;
}

.project-card .technologies span {
  color: #0d1330;
  font-weight: bold;
}
</style>
