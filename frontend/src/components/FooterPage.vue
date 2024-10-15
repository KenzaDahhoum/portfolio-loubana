<!-- src/components/FooterPage.vue -->
<template>
    <footer class="footer">
      <div class="footer-content">
        <div class="social-icons">
          <a href="https://instagram.com/oliban_loubana" target="_blank"><i class="fab fa-instagram"></i></a>
          <a href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i></a>
          <a href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin"></i></a>
        </div>
        <p>© 2024 Kenza's Portfolio. All Rights Reserved.</p>
      </div>
    </footer>
  </template>
  
  <style scoped>
  .footer {
    background-color: #0d1330;
    color: #fff;
    padding: 20px 0;
    text-align: center;
    font-size: 14px;
  }
  
  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .social-icons {
    margin-bottom: 10px;
  }
  
  .social-icons a {
    margin: 0 10px;
    color: #ffd600;
    font-size: 24px;
    transition: color 0.3s;
  }
  
  .social-icons a:hover {
    color: #f5f5dc;
  }
  
  p {
    margin: 0;
    font-size: 16px;
  }
  </style>
  