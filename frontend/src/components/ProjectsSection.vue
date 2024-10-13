<template>
    <div class="section projects-section">
      <h2>Projects</h2>
      <ul>
        <li v-for="project in projects" :key="project.id">
          <strong class="title">{{ project.title }}</strong> - {{ project.description }} ({{ project.technologies }})
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
  .projects-section ul {
    list-style: none;
    padding: 0;
  }
  
  .projects-section ul li {
    margin-bottom: 10px;
    font-size: 1.1rem;
  }
  
  .projects-section ul li strong.title {
    color: #ffd600;
    font-weight: bold;
  }
  
  .projects-section ul li:before {
    content: '•';
    color: #ffd600;
    font-weight: bold;
    display: inline-block;
    width: 1em;
    margin-left: -1em;
  }
  
  .projects-section ul li:hover {
    background-color: #f1f1f1;
    border-radius: 5px;
    transition: all 0.3s ease;
  }
  .card {
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
}

  </style>
  