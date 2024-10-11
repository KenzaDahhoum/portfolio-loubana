<template>
  <header class="header-section" data-aos="fade-up" data-aos-duration="2000" data-aos-once="true">
    <div class="header-overlay"></div>
    <div class="header-content">
      <h1>Welcome to Kenza's Portfolio</h1>
      <p>Discover my projects, creativity, and the passion behind my work.</p>
      <router-link to="/#projects" class="explore-button">Explore My Work</router-link>

    </div>
    <div class="header-graphics">
      <div class="emoji">✨</div>
      <div class="emoji">🚀</div>
      <div class="emoji">💻</div>
      <div class="emoji">🌟</div>
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
  background: url('../assets/images/glasses-lie-laptop-reflecting-light-from-screen-dark.jpg') no-repeat center center;
  background-size: cover;
  margin-top: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: #fafafa;
  position: relative;
  width: 100%;
  max-width: 100vw;
  overflow: hidden;
}

/* Background Overlay */
.header-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6); /* Adjust transparency for the effect */
  z-index: 1;
}

/* Header Content */
.header-content {
  color: #ffd600; /* Set text color to match theme */
  z-index: 2;
  font-family: 'Roboto', sans-serif;
}

.header-content h1 {
  font-size: 3.5rem;
  font-weight: bold;
  color: #fff;
}

.header-content p {
  font-size: 1.5rem;
  margin-top: 10px;
  color: #e0e0e0;
}

/* Explore Button Styling */
.explore-button {
  display: inline-block;
  margin-top: 20px;
  padding: 12px 24px;
  background-color: #ffd600;
  color: #1a237e;
  border: none;
  border-radius: 25px;
  font-size: 1.2rem;
  text-decoration: none;
  transition: background-color 0.3s ease, transform 0.3s ease;
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
}

.explore-button:hover {
  background-color: #f5f5dc;
  transform: translateY(-8px);
}

/* Emoji Styling */
.header-graphics {
  position: absolute;
  left: 5%;
  top: 30%;
  display: flex;
  flex-direction: column;
  gap: 15px;
  z-index: 2;
}

.emoji {
  font-size: 2.5rem;
  animation: float 4s ease-in-out infinite;
}

/* Float Animation */
@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .header-content h1 {
    font-size: 2.5rem;
  }

  .header-content p {
    font-size: 1rem;
  }

  .explore-button {
    font-size: 1rem;
    padding: 10px 20px;
  }

  .header-graphics {
    left: 2%;
    top: 20%;
  }

  .emoji {
    font-size: 1.5rem;
  }
}
</style>
