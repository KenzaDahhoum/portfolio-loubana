<template>
  <header class="header-section" data-aos="slide-left" data-aos-duration="2000" data-aos-once="true">
    <div class="header-content">
      <h1>Welcome to Kenza's Portfolio</h1>
      <p>Discover my projects, creativity, and the passion behind my work.</p>
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
/* Modern Minimalist Color Palette */
:root {
  --navy-blue: #1a237e;
  --cool-gray: #eceff1;
  --slate-gray: #607d8b;
  --soft-white: #fafafa;
  --accent-yellow: #ffd600;
  --warm-beige: #f5f5dc;
}

/* Header Styling */
.header-section {
  height: 75vh;
  background: url('../assets/images/bg-header.jpg') no-repeat center center / cover;
  margin-top: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding-top: 120px;
  color: var(--soft-white);
  box-shadow: 0 4px 6px rgba(96, 125, 139, 0.3);
  position: relative;
}

/* Header Content Styling */
.header-content {
  color: var(--navy-blue);
  z-index: 1;
  animation: fadeInContent 2s ease-in-out;
}

.header-content h1 {
  font-size: 3rem;
  color: var(--accent-yellow);
  margin-bottom: 20px;
}

.header-content p {
  font-size: 1.2rem;
  color: var(--slate-gray);
  max-width: 600px;
  margin: 0 auto;
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

/* Background Animation */
.header-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  height: 100%;
  width: 100%;
  background: rgba(255, 214, 0, 0.1);
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
