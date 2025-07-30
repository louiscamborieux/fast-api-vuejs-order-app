<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import productService from './services/productService'
import orderService from './services/orderService'
import navBar from './components/navBar.vue'
import ProductList from './components/ProductList.vue'

import {computed, onMounted, ref} from 'vue';
import NavBar from './components/navBar.vue'
const isLoading = ref(true);
const productsData = ref([]);
const categories = ref([]);


onMounted(async () => {
  const res = await productService.getAllProducts();
  const categoriesSet = new Set();
  productsData.value = res.data;
  productsData.value.forEach(p => categoriesSet.add(p.category))
  categories.value = Array.from(categoriesSet);


  console.log(res);

  const res2 = await productService.getAllProducts("electronics");
  console.log(res2)

  const res3 = await orderService.placeOrder("test",[1,2]);
  console.log(res2)

})

async function setFilter(category) {
  if (category.trim() == "") {
    category = undefined
  }
  const res = await productService.getAllProducts(category);
  productsData.value = res.data;
}

</script>

<template>
  <header>
    <NavBar />
  </header>

  <main>
    <router-view />
  </main>
</template>

<style>
  main {
    padding-top: 40px;
  }
</style>


