
import { createRouter, createWebHistory } from 'vue-router';
import Books from '../components/Books.vue';
import HelloWorld from '../components/HelloWorld.vue';

const routes = [
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: '/books',
    name: 'Books',
    component: Books
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;