<template>
    <b-navbar toggleable="lg" type="dark" variant="info" class="main-navbar" data-aos="fade-down">
      <b-container>
        <b-navbar-brand href="#">My Portfolio</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <b-nav-item href="#home">Home</b-nav-item>
            <b-nav-item href="#about">About Me</b-nav-item>
            <b-nav-item href="#projects">Projects</b-nav-item>
            <b-nav-item href="#contact">Contact</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </template>
  
  <script>
  import 'aos/dist/aos.css'; // Import AOS CSS
  import AOS from 'aos'; // Import AOS
  
  export default {
    mounted() {
      AOS.init(); // Initialize AOS animations
    },
  };
  </script>
  
  <style scoped>
  .main-navbar {
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
    transition: background-color 0.3s ease-in-out;
  }
  
  .main-navbar.scrolled {
    background-color: #0d6efd;
  }
  </style>
  