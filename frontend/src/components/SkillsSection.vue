<template>
    <div class="section skills-section">
      <h2>Skills</h2>
      <div class="dropdown" v-for="category in skillCategories" :key="category.title">
        <div class="dropdown-header" @click="toggleDropdown(category)">
          <i class="fas" :class="category.icon"></i>
          {{ category.title }}
          <span v-if="category.open" class="arrow">▲</span>
          <span v-else class="arrow">▼</span>
        </div>
        <ul v-if="category.open" class="dropdown-list">
          <li v-for="skill in category.skills" :key="skill.id">
            <strong>{{ skill.name }}</strong>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        skills: [],
        skillCategories: [
          { title: "Tools and Technology", open: false, skills: [], icon: "fa-tools" },
          { title: "Programming Languages", open: false, skills: [], icon: "fa-code" },
          { title: "Soft Skills", open: false, skills: [], icon: "fa-users" },
          { title: "Design Skills", open: false, skills: [], icon: "fa-paint-brush" },
        ],
      };
    },
    mounted() {
      this.fetchSkills();
    },
    methods: {
      async fetchSkills() {
        try {
          const response = await axios.get('https://kenzas-portfolio.onrender.com/api/skills');
          this.skills = response.data;
          this.assignSkillsToCategories();
        } catch (error) {
          console.error("Error fetching skills data", error);
        }
      },
      assignSkillsToCategories() {
        this.skillCategories.forEach((category) => {
          category.skills = this.skills.filter((skill) => skill.category === category.title);
        });
      },
      toggleDropdown(category) {
        category.open = !category.open;
      },
    },
  };
  </script>
  
  <style scoped>
  /* Skills Section Styles */
  
  .section h2 {
    color: #0d1330;
    font-size: 2.2rem;
    font-family: 'Pacifico', cursive;
    text-align: center;
    margin-bottom: 20px;
  }
  
  .skills-section {
    margin-bottom: 2rem;
  }
  
  /* Dropdown styling */
  .dropdown {
    margin-bottom: 20px;
    border-radius: 12px;
    background-color: #f0f4f7; /* Soft background color */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
  }
  
  .dropdown-header {
    padding: 15px 20px;
    font-size: 1.2rem;
    font-weight: bold;
    background-color: #f9f9f9;
    border-radius: 12px;
    cursor: pointer;
    color: #0d1330;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background-color 0.3s ease;
  }
  
  .dropdown-header:hover {
    background-color: #e0e7ff; /* Light blue hover effect */
  }
  
  .arrow {
    color: #888;
    transition: transform 0.3s ease;
  }
  
  .dropdown-list {
    list-style: none;
    padding: 0;
    margin: 10px 0;
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  }
  
  .dropdown-list li {
    padding: 12px 20px;
    font-size: 1.1rem;
    color: #333;
    transition: color 0.3s ease;
  }
  
  .dropdown-list li:hover {
    background-color: #f1f1f1;
    color: #0d1330;
  }
  
  i.fas {
    margin-right: 10px;
    color: #ffd600;
  }
  
  /* Responsive design */
  @media (max-width: 768px) {
    .dropdown-header {
      font-size: 1.1rem;
      padding: 12px 15px;
    }
  
    .dropdown-list li {
      font-size: 1rem;
    }
  }
  </style>
  