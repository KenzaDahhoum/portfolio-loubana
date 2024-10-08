<template>
    <div class="portfolio-container">
      <h2>Portfolio Projects</h2>
      <div class="project-card" v-for="project in portfolioProjects" :key="project.title">
        <h3>{{ project.title }}</h3>
        <p>{{ project.description }}</p>
        <a :href="project.link" target="_blank" class="project-link">View Project</a>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        portfolioProjects: []  // This will store the projects fetched from the backend
      };
    },
    mounted() {
      this.fetchPortfolioProjects();  // Fetch data when the component is mounted
    },
    methods: {
      fetchPortfolioProjects() {
        axios.get('http://127.0.0.1:5000/api/portfolio')  // Make a GET request to the Flask backend
          .then(response => {
            this.portfolioProjects = response.data;  // Store the data in the component's data property
          })
          .catch(error => {
            console.error('Error fetching portfolio projects:', error);
          });
      }
    }
  }
  </script>
  
  <style scoped>
  .portfolio-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
  }
  
  h2 {
    color: #2c3e50;
    margin-bottom: 30px;
  }
  
  .project-card {
    background-color: #f9f9f9;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    text-align: left;
  }
  
  .project-card h3 {
    margin-top: 0;
    color: #3498db;
  }
  
  .project-card p {
    margin: 10px 0;
  }
  
  .project-link {
    color: #3498db;
    text-decoration: none;
    font-weight: bold;
  }
  
  .project-link:hover {
    text-decoration: underline;
  }
  </style>
  