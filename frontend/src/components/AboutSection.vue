<template>
    <section class="about-section">
      <div class="about-container">
        <!-- Left Column: Text Content -->
        <div class="about-text">
          <h2>About Me</h2>
          <p>
            Hi, I'm <span class="highlight">Kenza</span>, a dedicated software developer with a passion for solving complex problems through technology. My journey in tech has been fueled by a deep curiosity and a drive to create meaningful solutions that make a difference.
          </p>
          <p>
            Over the years, I’ve honed my skills in <span class="highlight">web development</span>, <span class="highlight">software engineering</span>, and <span class="highlight">project management</span>, working on diverse projects that push the boundaries of innovation. From launching small businesses to collaborating with teams, my entrepreneurial mindset has enabled me to turn ideas into reality.
          </p>
          <p>
            I’m always exploring new challenges, eager to grow both personally and professionally. Whether it’s crafting a user-friendly web experience or building scalable applications, I strive to deliver excellence in everything I do. Ready to learn more about my journey and the exciting projects I’ve been a part of? Let's dive in!
          </p>
          <!-- Use router-link for navigation -->
          <router-link to="/my-journey" class="explore-btn">Explore More</router-link>
        </div>
  
        <!-- Right Column: Image -->
        <div class="about-image">
          <img src="../assets/images/kenza_cv-removebg-preview (1).png" alt="Kenza's Photo" />
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {};
  </script>
  
  <style scoped>
  
  .about-section {
    padding: 60px 20px;
    background-color: #f4f4f4;
    position: relative;
    overflow: hidden;
  }
  
  .about-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .about-text {
    flex: 1;
    min-width: 280px;
    margin-right: 40px;
  }
  
  .about-text h2 {
    font-family: 'Pacifico', cursive;
    font-size: 2.5rem;
    color: #0d1330;
    margin-bottom: 20px;
  }
  
  .about-text p {
    font-size: 1.1em;
    line-height: 1.6;
    color: #333;
    margin-bottom: 15px;
  }
  
  .highlight {
    color: #1a237e;
    font-weight: bold;
  }
  
  .about-image {
    flex: 1;
    min-width: 280px;
    text-align: center;
    max-width: 400px;
  }
  
  .about-image img {
    width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    object-fit: cover;
    max-height: 400px; 
    display: inline-block;
  }
  
  /* Button Style */
  .explore-btn {
    display: inline-block;
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #ffd600;
    color: #1a237e;
    font-weight: bold;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    text-decoration: none;
    transition: background-color 0.3s ease, transform 0.3s ease;
  }
  
  .explore-btn:hover {
    background-color: #f5f5dc;
    transform: translateY(-5px);
  }
  
  /* Responsive Design */
  @media (max-width: 768px) {
    .about-container {
      flex-direction: column;
      text-align: center;
    }
    .about-text {
      margin: 0 0 20px 0;
      text-align: center;
    }
    .about-image {
      margin: 0;
      max-width: 300px;
    }
  }
  </style>
  