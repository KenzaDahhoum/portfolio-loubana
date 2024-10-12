<template>
    <div class="education-section">
      <h2>Education</h2>
      <ul>
        <li v-for="education in educations" :key="education.id">
          <strong>{{ education.institution }}</strong> - {{ education.degree }} ({{ education.start_date }} - {{ education.end_date }})
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        educations: [],
      };
    },
    mounted() {
      this.fetchEducation();
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
    },
  };
  </script>
  
  <style scoped>
  .education-section {
    margin-bottom: 2rem;
  }
  </style>
  