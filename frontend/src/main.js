import { createApp } from 'vue';
import App from './App.vue';

// Import Bootstrap CSS and JS
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';

// Import specific components from BootstrapVueNext
import { BCard, BButton, BDropdown, BDropdownItem } from 'bootstrap-vue-next';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';

// Import AOS (Animate On Scroll)
import AOS from 'aos';
import 'aos/dist/aos.css';

// Import the router
import router from './router';

// Import Fontawsome
import '@fortawesome/fontawesome-free/css/all.css';


const app = createApp(App);

// Register specific BootstrapVueNext components globally
app.component('BCard', BCard);
app.component('BButton', BButton);
app.component('BDropdown', BDropdown);
app.component('BDropdownItem', BDropdownItem);

// Use the router
app.use(router);

// Initialize AOS
app.mount('#app');
AOS.init();
