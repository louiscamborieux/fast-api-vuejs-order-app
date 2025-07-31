import  { createRouter, createWebHistory  } from 'vue-router'
import ProductsPage  from '@/components/ProductsPage.vue'
import OrdersPage from '@/components/OrdersPage.vue';

const routes = [
    {path: '/products', component: ProductsPage, alias: '/'},
    {path: '/orders', component: OrdersPage},
    {path: '/:pathMatch(.*)*', redirect: '/'}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;