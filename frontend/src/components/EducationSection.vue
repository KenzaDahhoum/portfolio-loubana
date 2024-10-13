<template>
    <div class="section education-section">
      <h2>Education</h2>
      <ul>
        <li v-for="education in educations" :key="education.id">
          <strong class="institution">{{ education.institution }}</strong> - {{ education.degree }} ({{ education.start_date }} - {{ education.end_date }})
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
  .education-section ul {
    list-style: none;
    padding: 0;
  }
  
  .education-section ul li {
    margin-bottom: 10px;
    font-size: 1.1rem;
  }
  
  .education-section ul li strong.institution {
    color: #ffd600; /* Matching with your yellow theme */
    font-weight: bold;
  }
  
  .education-section ul li:before {
    content: '•';
    color: #ffd600;
    font-weight: bold;
    display: inline-block;
    width: 1em;
    margin-left: -1em;
  }
  
  .education-section ul li:hover {
    background-color: #f1f1f1;
    border-radius: 5px;
    transition: all 0.3s ease;
  }
  </style>
  