import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import JourneyPage from '../components/JourneyPage.vue';
import LoubanaPage from '@/components/LoubanaPage.vue';
const routes = [
  { path: '/', component: HomePage },
  { path: '/my-journey', component: JourneyPage },
  { path: '/loubana' , component: LoubanaPage}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else if (to.hash) {
      return { el: to.hash, behavior: 'smooth' };
    } else {
      return { top: 0 };
    }
  }
});

export default router;
