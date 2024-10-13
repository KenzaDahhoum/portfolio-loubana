<template>
    <div class="section education-section">
      <h2>Education</h2>
      <ul>
        <li v-for="education in educations" :key="education.id" class="education-card">
          <div class="education-details">
            <strong class="institution">{{ education.institution }}</strong>
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
  /* Education Section Styles */
  .education-section {
    margin-bottom: 2rem;
  }
  .section h2 {
  color: #0d1330;
  font-size: 2.2rem;
  font-family: 'Pacifico', cursive;
  margin-bottom: 20px;
  text-align: center;
}
  
  /* Education List Styling */
  ul {
    list-style: none;
    padding: 0;
  }
  
  .education-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding: 15px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease;
  }
  
  .education-card:hover {
    background-color: #f9f9f9;
  }
  
  /* Styling for the Education Details */
  .education-details {
    display: flex;
    flex-direction: column;
    margin-right: 15px;
  }
  
  /* Institution Name in Bold and Yellow */
  .institution {
    font-size: 1.2rem;
    color: #ffd600;
    font-weight: bold;
  }
  
  /* Degree Information */
  .degree {
    font-size: 1.1rem;
    color: #333;
  }
  
  /* Duration Styling (Dates) */
  .duration {
    font-size: 1rem;
    color: #888;
    font-style: italic;
  }
  
  /* Icon Styling */
  .duration i {
    margin-right: 8px;
    color: #ffd600;
  }
  
  /* Hover Effect */
  .education-card:hover .institution {
    color: #e0a800;
  }
  </style>
  