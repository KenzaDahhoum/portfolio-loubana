<template>
  <header class="header-section" data-aos="slide-left" data-aos-duration="2000" data-aos-once="true">
    <div class="header-content">
      <h1>Welcome to My Portfolio</h1>
      <p>Explore my work here.</p>
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
/* Header Styling */
.header-section {
  height: 75vh; /* Full viewport height */
  background-image: url('../assets/images/bg-header.jpg'); /* Update with your image path */
  background-size: cover !important;
  background-position: left; /* Start from the left */
  margin-top: 60px; /* Offset for the navbar height */
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding-top: 120px; 
  color: #fafafa; /* Soft White */
  box-shadow: 0 4px 6px rgba(96, 125, 139, 0.3); /* Slate Gray shadow */
  position: relative;
}

/* Header Content Styling */
.header-content {
  color: #fafafa; /* Soft White */
  z-index: 1;
  animation: fadeInContent 2s ease-in-out; /* Fade-in effect for content */
}

/* Fade-in effect for the content */
@keyframes fadeInContent {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Navbar Styling */
.navbar {
  background-color: #eceff1; /* Cool Gray */
  box-shadow: 0 2px 4px rgba(96, 125, 139, 0.3); /* Slate Gray shadow */
  display: flex;
  justify-content: space-around;
  padding: 10px 20px;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 1030;
  transition: background-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

/* Navbar Links Styling */
.navbar a {
  color: #607d8b; /* Slate Gray */
  text-decoration: none;
  font-weight: bold;
  padding: 10px;
  transition: color 0.3s ease-in-out;
}

.navbar a:hover {
  color: #ffd600; /* Accent Yellow */
}

/* Active Link Styling */
.navbar a.active {
  color: #ffd600; /* Accent Yellow */
  border-bottom: 2px solid #ffd600; /* Optional */
}

/* Background Animation */
.header-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  height: 100%;
  width: 100%;
  background: rgba(255, 214, 0, 0.1); /* Accent Yellow with opacity */
  animation: animateBg 10s linear infinite;
}

/* Animation Keyframes */
@keyframes animateBg {
  0% {
    left: -100%;
  }
  50% {
    left: 0;
  }
  100% {
    left: 100%;
  }
}
</style>
