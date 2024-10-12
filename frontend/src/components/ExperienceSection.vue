<template>
    <div class="experience-section">
      <h2>Experience</h2>
      <ul>
        <li v-for="experience in experiences" :key="experience.id">
          <strong>{{ experience.company }}</strong> - {{ experience.position }} ({{ experience.start_date }} - {{ experience.end_date }})
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        experiences: [],
      };
    },
    mounted() {
      this.fetchExperience();
    },
    methods: {
      async fetchExperience() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/experience');
          this.experiences = response.data;
        } catch (error) {
          console.error("Error fetching experience data", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .experience-section {
    margin-bottom: 2rem;
  }
  </style>
  