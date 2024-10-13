<template>
    <div class="section experience-section">
        <h2><i class="fas fa-briefcase"></i> Experience</h2>
      <ul>
        <li v-for="experience in experiences" :key="experience.id">
          <strong class="company">{{ experience.company }}</strong> - {{ experience.position }} ({{ experience.start_date }} - {{ experience.end_date }})
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import '@fortawesome/fontawesome-free/css/all.css';

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
  .experience-section ul {
    list-style: none;
    padding: 0;
  }
  
  .experience-section ul li {
    margin-bottom: 10px;
    font-size: 1.1rem;
  }
  
  .experience-section ul li strong.company {
    color: #ffd600;
    font-weight: bold;
  }
  
  .experience-section ul li:before {
    content: '•';
    color: #ffd600;
    font-weight: bold;
    display: inline-block;
    width: 1em;
    margin-left: -1em;
  }
  
  .experience-section ul li:hover {
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
  