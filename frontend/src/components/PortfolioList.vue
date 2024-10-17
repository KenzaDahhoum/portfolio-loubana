<template>
  <section class="loubana-section">
    <div class="loubana-container">
      <!-- Title and Description -->
      <div class="loubana-text">
        <h2>Loubana</h2>
        <p>
          Loubana is more than just skincare; it's a commitment to bringing natural, effective, and luxurious care to your skin. Inspired by traditional Moroccan beauty secrets and modern skincare needs, Loubana products are crafted with pure oliban extract and precious oils. From revitalizing masques to hydrating creams, every product is designed to rejuvenate your skin, promote radiance, and enhance your natural glow. Our products are not only a treat for your skin but also a promise of quality, care, and sustainability, ensuring that your skin looks and feels its best with every use.
        </p>
      </div>
      
      <!-- Product Cards -->
      <div class="loubana-products">
        <div class="product-card" v-for="product in products" :key="product.id">
          <!-- Image -->
          <div class="product-image">
            <img :src="product.image" alt="Product Image" />
          </div>
          <!-- Text -->
          <div class="product-info">
            <h3>{{ product.title }}</h3>
            <p>{{ product.description }}</p>
          </div>
        </div>
      </div>

      <!-- Explore Button -->
      <router-link to="/loubana" class="explore-btn">Explore Loubana</router-link>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      products: [
        {
          id: 1,
          title: "Masque Oliban Miel",
          description: "A revitalizing masque enriched with oliban and honey.",
          image: require('@/assets/images/IMG_masque-1.jpeg'),
        },
        {
          id: 2,
          title: "Crème Oliban",
          description: "A deeply hydrating night cream with oliban and precious oils.",
          image: require('@/assets/images/IMG_creme-1.jpeg'),
        },
        {
          id: 3,
          title: "Tabrima",
          description: "A luxurious traditional scrub enriched with herbs for a radiant glow.",
          image: require('@/assets/images/tabrima.jpeg'),
        }
      ],
    };
  }
};
</script>

<style scoped>
.loubana-section {
  padding: 60px 20px;
  background-color: #f4f4f4;
  text-align: center;
}

.loubana-container {
  max-width: 1200px;
  margin: 0 auto;
}

.loubana-text h2 {
  font-family: 'Pacifico', cursive;
  font-size: 2.5rem;
  margin-bottom: 20px;
  color: #0d1330;
}

.loubana-text p {
  font-size: 1.1em;
  margin-bottom: 30px;
  color: #333;
}

.loubana-products {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.product-card {
  flex: 1;
  max-width: 300px;
  margin: 15px;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.product-card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}

.product-image img {
  width: 100%;
  height: auto;
  border-radius: 10px;
}

.product-info h3 {
  font-size: 1.5rem;
  margin: 15px 0 10px;
  font-weight: bold;
  color: #ffd600;
}

.product-info p {
  font-size: 1rem;
  color: #666;
}

.explore-btn {
    display: inline-block;
    margin-top: 25px;
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
</style>
