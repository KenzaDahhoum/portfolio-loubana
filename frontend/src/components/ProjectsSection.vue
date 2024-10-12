<template>
    <div class="projects-section">
      <h2>Projects</h2>
      <ul>
        <li v-for="project in projects" :key="project.id">
          <strong>{{ project.title }}</strong> - {{ project.description }} ({{ project.technologies }})
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        projects: [],
      };
    },
    mounted() {
      this.fetchProjects();
    },
    methods: {
      async fetchProjects() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/projects');
          this.projects = response.data;
        } catch (error) {
          console.error("Error fetching projects data", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .projects-section {
    margin-bottom: 2rem;
  }
  </style>
  