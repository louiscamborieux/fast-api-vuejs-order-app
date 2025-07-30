<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import productService from './services/productService'
import orderService from './services/orderService'
import ProductItem from './components/ProductItem.vue'
import ProductList from './components/ProductList.vue'
import axios from 'axios'

import {computed, onMounted, ref} from 'vue';
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
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
      <div v-if="loading">Loading...</div>


      <div v-else>
        <div>
          <h2>Pick a category</h2>
          <select class="category-select" @change="e => setFilter(e.target.value)" >
            <option value="">All</option>
            <option v-for="category in categories" :key="category" :value="category">{{category}}</option>
          </select>
        </div>
        <ProductList :items="productsData"/>
      </div>


  </main>
</template>

<style scoped>

.category-select {
  min-width: 200px;
  min-height: 50px;
  background-color: var(--color-background-soft);
  color: var(--color-text);
  font-size: large;
  border-radius: 8px;
}

.category-select option {
    background-color: var(--color-background-soft);
    font-size: large;
    border-radius: 8px;

}

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
