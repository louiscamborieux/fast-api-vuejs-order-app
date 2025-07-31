import  { createRouter, createWebHistory  } from 'vue-router'
import ProductsPage  from '@/components/ProductsPage.vue'
import OrdersPage from '@/components/OrdersPage.vue';

const routes = [
    {path: '/', component: ProductsPage},
    {path: '/products', component: ProductsPage},
    {path: '/orders', component: OrdersPage}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;