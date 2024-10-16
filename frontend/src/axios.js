import axios from 'axios';

// Create an instance of Axios with the base URL
const apiClient = axios.create({
  baseURL: 'https://kenzas-portfolio.onrender.com/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;
