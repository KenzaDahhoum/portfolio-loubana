<!-- JourneyPage.vue -->
<template>
    <div class="journey-page">
      <h2>My Journey</h2>
      <div class="journey-sections">
        <section>
          <h3>Education</h3>
          <p>Details about your educational background...</p>
        </section>
        <section>
          <h3>Work Experience</h3>
          <p>Details about your work experiences...</p>
        </section>
        <section>
          <h3>Internships</h3>
          <p>Details about your internships...</p>
        </section>
        <section>
          <h3>Training</h3>
          <p>Details about your training and courses...</p>
        </section>
        <section>
          <h3>Projects</h3>
          <p>Details about the projects you've developed during your studies...</p>
        </section>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "JourneyPage",
  };
  </script>
  
  <style scoped>
  .journey-page {
    padding: 60px 20px;
    background-color: #f4f4f4;
    color: #1a237e;
  }
  
  .journey-sections section {
    margin-bottom: 40px;
  }
  
  .journey-sections h3 {
    color: #607d8b;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .journey-sections p {
    font-size: 1.1em;
    line-height: 1.6;
  }
  </style>
  