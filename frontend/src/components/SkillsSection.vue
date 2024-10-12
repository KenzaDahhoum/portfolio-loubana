<template>
    <div class="skills-section">
      <h2>Skills</h2>
  
      <div class="skills-category" v-for="category in skillCategories" :key="category.name">
        <div class="skills-category-title" @click="toggleCategory(category.name)">
          {{ category.name }}
          <span v-if="isOpen(category.name)">▲</span>
          <span v-else>▼</span>
        </div>
        <ul v-if="isOpen(category.name)" class="skills-category-content">
          <li v-for="skill in category.skills" :key="skill.id">
            <strong>{{ skill.name }}</strong> - {{ skill.category }}
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
        openCategories: [],
      };
    },
    computed: {
      skillCategories() {
        // Group skills by category
        const categories = {};
        this.skills.forEach(skill => {
          if (!categories[skill.category]) {
            categories[skill.category] = [];
          }
          categories[skill.category].push(skill);
        });
  
        return Object.keys(categories).map(category => ({
          name: category,
          skills: categories[category],
        }));
      },
    },
    mounted() {
      this.fetchSkills();
    },
    methods: {
      async fetchSkills() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/skills');
          this.skills = response.data;
        } catch (error) {
          console.error('Error fetching skills data', error);
        }
      },
      toggleCategory(categoryName) {
        if (this.isOpen(categoryName)) {
          this.openCategories = this.openCategories.filter(cat => cat !== categoryName);
        } else {
          this.openCategories.push(categoryName);
        }
      },
      isOpen(categoryName) {
        return this.openCategories.includes(categoryName);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add styles here for your dropdown effect, it's included in the main page for now */
  </style>
  