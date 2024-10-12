import axios from 'axios';

// Create an instance of Axios with the base URL
const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;
