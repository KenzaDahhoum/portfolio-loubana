<template>
    <div class="masque-section">
      <div class="image-container">
        <img src="@/assets/images/IMG_masque-1.jpeg" alt="Masque Oliban" />
        <img src="@/assets/images/IMG_masque-2.jpeg" alt="Masque Oliban" />
        <img src="@/assets/images/IMG_masque-3.jpeg" alt="Masque Oliban" />
      </div>
      <div class="details">
        <h2>{{ product.title }}</h2>
        <p><strong>Benefits:</strong> {{ product.benefits }}</p>
        <p><strong>How to Use:</strong> {{ product.how_to_use }}</p>
        <p><strong>Ingredients:</strong></p>
        <ul>
          <li v-for="(ingredient, index) in product.ingredients" :key="index">
            {{ ingredient.name }} - {{ ingredient.benefits }}
          </li>
        </ul>
        <div class="buttons">
          <a :href="whatsAppLink" class="order-btn">Order via WhatsApp</a>
          <a :href="instagramLink" class="order-btn">Order via Instagram</a>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        product: {},
        whatsAppLink: ' https://wa.me/212644152668 ',
        instagramLink: 'https://www.instagram.com/oliban_loubana/',
      };
    },
    created() {
      axios.get('https://kenzas-portfolio.onrender.com/api/loubana/masque')
        .then(response => {
          this.product = response.data;
        })
        .catch(error => {
          console.error('Error fetching product data:', error);
        });
    },
  };
  </script>
  
  <style scoped>
  .masque-section {
    margin-top: 50px;
    text-align: center;
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
  .image-container img:hover {
  transform: scale(1.05);
  }
  .details {
    margin-top: 30px;
    text-align: left;
  }
  
  ul {
    padding-left: 20px;
  }
  
  .buttons {
    margin-top: 20px;
  }
  
  .order-btn {
  display: inline-block;
  margin-top: 25px;
  margin-left: 20px;
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
  .order-btn:hover{
    background-color: #f5f5dc;
    transform: translateY(-5px);
  
  }
  
  @media (max-width: 768px) {
  .image-container {
    flex-direction: column;
    gap: 30px;
  }
  
  .image-container img {
    width: 100%; 
  }
}

  </style>
  