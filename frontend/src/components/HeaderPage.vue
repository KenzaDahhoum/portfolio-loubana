<template>
  <header class="header-section" data-aos="slide-left" data-aos-duration="2000" data-aos-once="true">
    <div class="header-shapes">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="shape shape-3"></div>
      <div class="shape shape-4"></div>
    </div>
    <div class="header-content">
      <h1>Welcome to Kenza's Portfolio</h1>
      <p>Discover my projects, creativity, and the passion behind my work.</p>
      <a href="#projects" class="animated-button">Explore My Work</a> <!-- Animated Button -->
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
/* Updated Header Section with Minimalist Palette */
.header-section {
  height: 75vh;
  background-image: url('../assets/images/bg-header.jpg');
  background-size: cover;
  background-position: center;
  margin-top: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding-top: 120px;
  color: #fafafa;
  position: relative;
  overflow: hidden;
}

/* Geometric Shapes Styling */
.header-shapes .shape {
  position: absolute;
  opacity: 0.3;
  animation: animateShapes 8s infinite alternate;
}

/* First Shape (Triangle) */
.shape-1 {
  width: 0;
  height: 0;
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-bottom: 100px solid #607d8b; /* Slate Gray */
  top: 30%;
  right: 5%;
}

/* Second Shape (Hexagon) */
.shape-2 {
  width: 100px;
  height: 100px;
  background-color: #ffd600; /* Accent Yellow */
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  top: 50%;
  right: 20%;
}

/* Third Shape (Diamond) */
.shape-3 {
  width: 120px;
  height: 120px;
  background-color: #1a237e; /* Navy Blue */
  transform: rotate(45deg);
  top: 70%;
  right: 10%;
  opacity: 0.2;
}

/* Fourth Shape (Square) */
.shape-4 {
  width: 100px;
  height: 100px;
  background-color: #eceff1; /* Cool Gray */
  bottom: 15%;
  right: 5%;
  opacity: 0.4;
}

/* Animations */
@keyframes animateShapes {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(15px);
  }
}

/* Text Styling */
.header-content {
  color: #1a237e; /* Navy Blue */
  z-index: 1;
}

/* Animated Button Styling */
.animated-button {
  display: inline-block;
  margin-top: 20px;
  padding: 12px 24px;
  font-size: 1.1rem;
  font-weight: bold;
  color: #1a237e;
  background-color: #ffd600; /* Accent Yellow */
  border: none;
  border-radius: 25px;
  text-decoration: none;
  transition: all 0.3s ease-in-out;
  cursor: pointer;
}

/* Button Hover Effect */
.animated-button:hover {
  background-color: #1a237e;
  color: #ffd600;
  transform: scale(1.05);
}

/* Button Focus Effect */
.animated-button:focus {
  outline: none;
}
</style>
