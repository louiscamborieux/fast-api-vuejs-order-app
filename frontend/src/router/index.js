import  { createRouter, createWebHistory  } from 'vue-router'
import ProductsPage  from '@/components/ProductsPage.vue'

const routes = [
    {path: '/', component: ProductsPage},
    {path: '/products', component: ProductsPage}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;