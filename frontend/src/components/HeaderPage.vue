<template>
  <header class="header-section" data-aos="slide-left" data-aos-duration="2000" data-aos-once="true">
    <div class="header-shapes">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="shape shape-3"></div>
      <div class="shape shape-4"></div>
      <div class="hexagon"></div>
    </div>
    <div class="header-content">
      <h1>Welcome to Kenza's Portfolio</h1>
      <p>Discover my projects, creativity, and the passion behind my work.</p>
      <a href="#projects" class="explore-button">Explore My Work</a>
    </div>
  </header>
</template>

<script>
import AOS from 'aos';
import 'aos/dist/aos.css';

export default {
  mounted() {
    AOS.init({
      duration: 800,
      easing: 'ease-in-out',
    });
  },
};
</script>

<style scoped>
/* Prevent horizontal scroll */
body, html {
  overflow-x: hidden;
  margin: 0;
  padding: 0;
}

/* Header Section */
.header-section {
  height: 75vh;
  background: url('../assets/images/bg-header.jpg') no-repeat center center;
  background-size: cover;
  margin-top: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 0 20px; /* Added padding to avoid overflow */
  color: #fafafa;
  position: relative;
  width: 100%;
  max-width: 100vw; /* Ensures no overflow */
  overflow: hidden;
}

/* Shapes Styling */
.header-shapes .shape {
  position: absolute;
  opacity: 0.2;
}

/* Individual Shape Styles */
.shape-1 {
  width: 100px;
  height: 100px;
  background-color: #607d8b;
  top: 20%;
  left: 50%;
  border-radius: 50%;
}

.shape-2 {
  width: 150px;
  height: 150px;
  background-color: #ffd600;
  bottom: 15%;
  right: 10%; /* Adjusted to ensure no overflow */
  border-radius: 50%;
}

.shape-3 {
  width: 100px;
  height: 100px;
  background-color: #1a237e;
  top: 70%;
  left: 40%;
  right: 5%;
  transform: rotate(45deg);
}

.shape-4 {
  width: 70px;
  height: 70px;
  background-color: #f5f5dc;
  bottom: 30%;
  left: 40%; /* Adjusted to ensure no overflow */
  border-radius: 50%;
}

/* Hexagon Style */
.hexagon {
  width: 100px;
  height: 100px;
  background-color: #9e9e9e;
  clip-path: polygon(50% 0%, 93% 25%, 93% 75%, 50% 100%, 7% 75%, 7% 25%);
  top: 60%;
  right: 30%; /* Adjusted to ensure no overflow */
  position: absolute;
}

/* Header Content */
.header-content {
  color: #1a237e;
  z-index: 1;
}

.explore-button {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #ffd600;
  color: #1a237e;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  text-decoration: none;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.explore-button:hover {
  background-color: #f5f5dc;
  transform: translateY(-5px);
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .shape-1, .shape-2, .shape-3, .shape-4, .hexagon {
    display: none; /* Hide shapes on smaller screens */
  }

  .explore-button {
    font-size: 0.8rem;
    padding: 8px 15px;
  }
}
</style>
