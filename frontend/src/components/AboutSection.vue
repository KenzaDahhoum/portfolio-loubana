<template>
    <section class="about-section">
      <div class="about-container">
        <!-- Left Column: Text Content -->
        <div class="about-text">
          <h2>About Me</h2>
          <p>
            Hi, I'm <span class="highlight">Kenza</span>, a passionate developer and entrepreneur.
            My journey began with a love for technology and a desire to create
            meaningful solutions. Throughout my studies and experiences, I've
            developed a range of skills in <span class="highlight">web development</span>,
            <span class="highlight">software engineering</span>, and
            <span class="highlight">project management</span>. My entrepreneurial spirit has led me
            to start small businesses, where I apply my technical skills and
            creativity to solve real-world problems.
          </p>
          <p>
            Whether working on a personal project, collaborating with a team, or
            building my business, I strive to combine <span class="highlight">innovation</span> with practical
            solutions. I’m always eager to learn, grow, and take on new challenges
            that push my limits. Let's explore my work together!
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
  @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
  
  .about-section {
    padding: 60px 20px;
    background-color: #f4f4f4;
    position: relative;
    overflow: hidden;
  }
  
  .about-container {
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-wrap: wrap;
  }
  
  .about-text {
    flex: 1;
    min-width: 300px;
    margin-right: 20px;
  }
  
  .about-text h2 {
    font-family: 'Pacifico', cursive;
    font-size: 2.2rem;
    color: #0d1330;
    margin-bottom: 20px;
  }
  
  .about-text p {
    font-size: 1.1em;
    line-height: 1.6;
    color: #333;
  }
  
  .highlight {
    color: #ffd600;
    font-weight: bold;
  }
  
  .about-image {
    flex: 1;
    min-width: 300px;
    text-align: center;
  }
  
  .about-image img {
    width: 80%;
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  }
  
  /* Updated button style */
  .explore-btn {
    display: inline-block;
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #ffd600;
    color: #1a237e;
    font-weight: bold;
    border: none;
    border-radius: 5px;
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
    }
    .about-text {
      margin: 0;
    }
  }
  </style>
  