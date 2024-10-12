<template>
  <div class="journey-page">
    <section id="education" class="section">
      <h2>Education</h2>
      <ul>
        <li v-for="education in educations" :key="education.id">
          <strong>{{ education.institution }}</strong> - {{ education.degree }} ({{ education.start_date }} - {{ education.end_date }})
        </li>
      </ul>
    </section>

    <section id="experience" class="section">
      <h2>Experience</h2>
      <ul>
        <li v-for="experience in experiences" :key="experience.id">
          <strong>{{ experience.company }}</strong> - {{ experience.position }} ({{ experience.start_date }} - {{ experience.end_date }})
        </li>
      </ul>
    </section>

    <section id="projects" class="section">
      <h2>Projects</h2>
      <ul>
        <li v-for="project in projects" :key="project.id">
          <strong>{{ project.title }}</strong> - {{ project.description }} ({{ project.technologies }})
        </li>
      </ul>
    </section>

    <section id="skills" class="section">
      <h2>Skills</h2>
      <!-- Dropdowns for each category -->
      <div class="dropdown" v-for="category in skillCategories" :key="category.title">
        <div class="dropdown-header" @click="toggleDropdown(category)">
          {{ category.title }}
          <span v-if="category.open">▲</span>
          <span v-else>▼</span>
        </div>
        <ul v-if="category.open" class="dropdown-list">
          <li v-for="skill in category.skills" :key="skill.id">
            <strong>{{ skill.name }}</strong> - {{ skill.category }}
          </li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      educations: [],
      experiences: [],
      projects: [],
      skills: [],
      skillCategories: [
        { title: "Tools and Technology", open: false, skills: [] },
        { title: "Programming Languages", open: false, skills: [] },
        { title: "Soft Skills", open: false, skills: [] },
        { title: "Design Skills", open: false, skills: [] },
      ]
    };
  },
  mounted() {
    this.fetchEducation();
    this.fetchExperience();
    this.fetchProjects();
    this.fetchSkills();
  },
  methods: {
    async fetchEducation() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/education');
        this.educations = response.data;
      } catch (error) {
        console.error("Error fetching education data", error);
      }
    },
    async fetchExperience() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/experience');
        this.experiences = response.data;
      } catch (error) {
        console.error("Error fetching experience data", error);
      }
    },
    async fetchProjects() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/projects');
        this.projects = response.data;
      } catch (error) {
        console.error("Error fetching projects data", error);
      }
    },
    async fetchSkills() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/skills');
        this.skills = response.data;
        this.assignSkillsToCategories();
      } catch (error) {
        console.error("Error fetching skills data", error);
      }
    },
    assignSkillsToCategories() {
      this.skillCategories.forEach(category => {
        category.skills = this.skills.filter(skill => skill.category === category.title);
      });
    },
    toggleDropdown(category) {
      category.open = !category.open;
    }
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
  text-align: center; /* Centered title */
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

/* List styling */
ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  font-size: 1.1rem;
  color: #333;
}

li strong {
  color: #ffd600;
}

/* Custom dropdown list */
.dropdown {
  margin-bottom: 20px;
}

.dropdown-header {
  background-color: #ffd600;
  padding: 10px;
  border-radius: 8px;
  cursor: pointer;
  color: #0d1330;
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dropdown-list {
  list-style: none;
  padding-left: 20px;
  margin-top: 10px;
}

.dropdown-list li {
  margin-bottom: 5px;
  font-size: 1.1rem;
  color: #333;
  transition: all 0.3s ease;
}

.dropdown-list li:hover {
  color: #ffd600;
}

/* Responsive design */
@media (max-width: 768px) {
  .section {
    padding: 30px 15px;
  }
  
  .section h2 {
    font-size: 1.8rem;
  }

  li {
    font-size: 1rem;
  }
}
</style>
