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
  height: 100vh;
  background-color: #f8f9fa; /* Light background */
  background-image: url('../assets/images/bg-header.jpg'); /* Add your image here */
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

</style>
