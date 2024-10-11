import { createApp } from 'vue';
import App from './App.vue';

// Import Bootstrap and BootstrapVueNext
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import { BootstrapVueNext } from 'bootstrap-vue-next';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';

// Import AOS
import AOS from 'aos';
import 'aos/dist/aos.css';

// Import the router
import router from './router';

const app = createApp(App);

// Use BootstrapVueNext
app.use(BootstrapVueNext);

// Use the router
app.use(router);

// Initialize AOS
app.mount('#app');
AOS.init();
