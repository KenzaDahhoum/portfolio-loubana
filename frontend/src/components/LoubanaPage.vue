<template>
  <div class="loubana-page">
    <!-- Welcome Section -->
    <div class="welcome-section">
      <h1>Welcome to Loubana Skincare</h1>
      <p>
        Discover our luxurious, natural skincare products designed with pure oliban extract and precious oils. Rejuvenate, nourish, and pamper your skin with our handcrafted formulations.
      </p>
    </div>

    <!-- Crème Section -->
    <div class="product-section">
      <CremeSection />
    </div>

    <!-- Masque Section -->
    <div class="product-section">
      <MasqueSection />
    </div>

    <!-- Tabrima Section -->
    <div class="product-section">
      <TabrimaSection />
    </div>
  </div>
</template>

<script>
import CremeSection from './CremeSection.vue';
import MasqueSection from './MasqueSection.vue';
import TabrimaSection from './TabrimaSection.vue';

export default {
  components: {
    CremeSection,
    MasqueSection,
    TabrimaSection,
  },
};
</script>

<style scoped>
.loubana-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 60px 20px;
}

.welcome-section {
  text-align: center;
  margin-bottom: 30px;
}

.welcome-section h1 {
  font-size: 3rem;
  color: #ffcc00;
  text-align: center;
  margin-top: 40px;
  font-family: 'Pacifico', cursive;
  letter-spacing: 2px;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}

.welcome-section p {
  font-size: 1.2rem;
  color: #333;
  max-width: 700px;
  margin: 20px auto;
  line-height: 1.6;
}

.product-section {
  width: 80%;
  background-color: #f9f9f9;
  margin: 20px 0;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  padding: 40px 20px;
  text-align: center;
}

.order-btn {
  background-color: #0d1330;
  color: white;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  cursor: pointer;
  font-weight: bold;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.order-btn:hover {
  background-color: #ffd600;
  color: #0d1330;
}

.image-container {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap; 
}

.image-container img {
  width: 200px;
  height: auto;
  border-radius: 10px;
  transition: transform 0.3s ease-in-out;
}

@media (max-width: 768px) {
  .image-container {
    flex-direction: column; 
    gap: 10px;
  }
  
  .image-container img {
    width: 100%; 
  }
}

</style>
