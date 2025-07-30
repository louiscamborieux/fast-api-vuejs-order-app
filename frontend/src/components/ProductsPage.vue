<script setup>
import productService from '../services/productService'
import orderService from '../services/orderService'
import ProductList from './ProductList.vue'

import {onMounted, ref, watch} from 'vue';
const isLoading = ref(true);
const failedLoading = ref(false)
const productsData = ref([]);
const categories = ref([]);
const selected = ref([]);
const isError = ref(false);
const customer_name = ref('');
const error_message = ref('');


onMounted(async () => {
  try {
    const res = await productService.getAllProducts();
    const categoriesSet = new Set();
    productsData.value = res.data;
    productsData.value.forEach(p => categoriesSet.add(p.category))
    categories.value = Array.from(categoriesSet);
  }
  catch (error) {
    isError.value = true;
    failedLoading.value = true;
    error_message.value = "An unknown error has occured ("+error.status+" : "+error.code+")"
  }
  finally {
    isLoading.value = false;
  }

})

async function setFilter(category) {
  if (category.trim() == "") {
    category = undefined
  }
  selected.value = [];
  const res = await productService.getAllProducts(category);
  productsData.value = res.data;
}

async function handleOrder() {
  try {
    const res = await orderService.placeOrder(customer_name.value,selected.value);
  }
  catch (error) {
    
    switch (error.status) {
      case 400 :
        error_message.value = "Please provide a non-empty customer name."
        break;
      case 404 :
        error_message.value = "Some selected items do not exist."
        break;
      default :
        error_message.value = "An unknown error has occured ("+error.status+")"
    }

    console.log(error.status)
    isError.value = true;
  }

  
}

watch(selected, (newVal) => {
    console.log('Selected IDs:', newVal, 'Length:', newVal.length);
})


watch(isError, (newVal) => {
    console.log(newVal)
})
</script>

<template>
  <main>
    <h1>Product List</h1>
      <div v-if="isLoading">Loading...</div>

      <div v-else-if="!failedLoading">
        <div id="product-category-filter-div">
          <label for="product-category-filter">Pick a category</label>

          <select name="product-category-filter" class="category-select" @change="e => setFilter(e.target.value)" >
            <option value="">All</option>
            <option v-for="category in categories" :key="category" :value="category">{{category}}</option>
          </select>
        </div>
        <div>
          <p>Click to select items</p>
        </div>
        <ProductList :items="productsData" v-model:selected="selected"/>

        <form @submit.prevent="handleOrder" id="order-form" class="centered">
          <div class="centered">
            <label for="customer_name">Customer name</label>
            <input v-model="customer_name" type="text" required />
          </div>

          <button type="submit" id="submit-order">Place Order</button>
        </form>

        
      </div>
      <div v-if="isError" id="error_div">{{ error_message  }} </div>

  </main>
</template>

<style scoped>

#error_div {
  background-color: #ba3434;
  height: 50px;
  padding: 5px;

  color: var(--vt-c-white);
  font-weight: bold;
}

main {
    width: 100%;
    padding-bottom: 12px;
}

p {
  font-size: large;
}

.centered {
  font-size: large;
  text-align: center;
}

#product-category-filter-div {
    margin-bottom: 12px;
    display: flex;
    justify-content: center;
}

label {
    font-size: large;
    padding: 12px;
}

#order-form input[type=text],  #order-form button[type=submit]{
  min-width: 200px;
  min-height: 50px;
  background-color: var(--color-background-soft);
  border: none;
  color: var(--color-text);
  font-size: large;
}

#order-form #submit-order:hover {
  background-color: var(--color-background-mute);
}

#order-form div {
  margin-bottom: 15px;
}

.category-select{
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

h1 {
    font-size: 45px;
    text-align: center;
}
</style>
