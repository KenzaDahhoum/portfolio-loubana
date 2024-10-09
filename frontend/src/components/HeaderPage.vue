<template>
  <header class="header-section">
    <div class="header-content">
      <h1>Welcome to My Portfolio</h1>
      <p>Explore my work here.</p>
    </div>
  </header>
</template>

<script>
export default {
  name: 'HeaderPage',
};
</script>

<style scoped>
.header-section {
  height: 75vh;
  background-image: url('../assets/images/bg-header.jpg'); 
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding-top: 120px; 
}

.header-content h1 {
  font-size: 3.5rem;
  color: #ffffff;
}

.header-content p {
  font-size: 1.25rem;
  color: #f0f0f0;
}
</style>
