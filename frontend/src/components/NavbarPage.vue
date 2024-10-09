<template>
  <b-navbar toggleable="lg" type="dark" variant="info" class="main-navbar fixed-top">
    <b-container>
      <div class="navbar-wrapper mx-auto d-flex justify-content-between align-items-center">
        <b-navbar-brand href="#" class="navbar-title">
          Kenza's Portfolio
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="d-flex justify-content-center">
            <a href="#home" class="nav-link-item">Home</a>
            <a href="#about" class="nav-link-item">About Me</a>
            <a href="#projects" class="nav-link-item">Projects</a>
            <a href="#contact" class="nav-link-item">Contact</a>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-container>
  </b-navbar>
</template>


<script>
import 'aos/dist/aos.css'; 
import AOS from 'aos'; 

export default {
  mounted() {
    AOS.init();
  },
};
</script>

<style scoped>
.main-navbar {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 1000;
  background-color: #0d6efd;
  padding: 10px 20px;
}

.navbar-title {
  font-family: 'Pacifico', cursive;
  font-size: 1.8rem;
  font-weight: bold;
  color: #fff;
}

.b-navbar-nav {
  display: flex;
  justify-content: center;
  align-items: center;
}

.nav-link-item {
  font-size: 1.2rem;
  color: #fff;
  margin: 0 20px;
  transition: color 0.3s ease-in-out;
  cursor: pointer;
}

.nav-link-item:hover {
  color: #ffc107;
  text-decoration: underline;
}
</style>
