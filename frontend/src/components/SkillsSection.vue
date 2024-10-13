<template>
    <div class="section skills-section">
      <h2>Skills</h2>
      <div class="dropdown" v-for="category in skillCategories" :key="category.title">
        <div class="dropdown-header" @click="toggleDropdown(category)">
          {{ category.title }}
          <span v-if="category.open">▲</span>
          <span v-else>▼</span>
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
          { title: "Tools and Technology", open: false, skills: [] },
          { title: "Programming Languages", open: false, skills: [] },
          { title: "Soft Skills", open: false, skills: [] },
          { title: "Design Skills", open: false, skills: [] },
        ]
      };
    },
    mounted() {
      this.fetchSkills();
    },
    methods: {
      async fetchSkills() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/skills');
          this.skills = response.data;
          this.assignSkillsToCategories();
        } catch (error) {
          console.error("Error fetching skills data", error);
        }
      },
      assignSkillsToCategories() {
        this.skillCategories.forEach(category => {
          category.skills = this.skills.filter(skill => skill.category === category.title);
        });
      },
      toggleDropdown(category) {
        category.open = !category.open;
      }
    },
  };
  </script>
  
  <style scoped>
  /* Dropdown Styling */
  .dropdown {
    margin-bottom: 20px;
  }
  
  .dropdown-header {
    background-color: #ffd600;
    padding: 15px;
    border-radius: 8px;
    cursor: pointer;
    color: #0d1330;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .dropdown-list {
    list-style: none;
    padding-left: 20px;
    margin-top: 10px;
  }
  
  .dropdown-list li {
    margin-bottom: 5px;
    font-size: 1.1rem;
    color: #333;
  }
  
  .dropdown-list li:hover {
    color: #ffd600;
  }
  
  .dropdown-header:hover {
    background-color: #ffe680;
  }
  </style>
  