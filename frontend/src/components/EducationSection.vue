<template>
    <div class="section education-section">
      <h2>Education</h2>
      <ul>
        <li 
          v-for="education in educations" 
          :key="education.id" 
          class="education-card"
          data-aos="zoom-in-up"
        >
          <div class="education-details">
            <strong class="institution">{{ education.institution }}</strong>
            <br>
            <span class="degree">{{ education.degree }}</span>
          </div>
          <div class="duration">
            <i class="fas fa-calendar-alt"></i> {{ education.start_date }} - {{ education.end_date }}
          </div>
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
          const response = await axios.get('https://kenzas-portfolio.onrender.com/api/education');
          this.educations = response.data;
        } catch (error) {
          console.error("Error fetching education data", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .section h2 {
  color: #0d1330;
  font-size: 2.2rem;
  font-family: 'Pacifico', cursive;
  margin-bottom: 20px;
  text-align: center;
}
  .education-section {
    margin-bottom: 2rem;
  }
  
  .education-card {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
    padding: 15px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .institution {
    font-size: 1.2rem;
    color: #ffd600;
    font-weight: bold;
  }
  
  .degree {
    font-size: 1.1rem;
    color: #333;
  }
  
  .duration {
    font-size: 1rem;
    color: #888;
    font-style: italic;
  }
  
  .duration i {
    margin-right: 8px;
    color: #ffd600;
  }
  
  .education-card:hover {
    background-color: #f9f9f9;
  }
  </style>
  