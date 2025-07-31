<template>
  <main>
    <h1>{{title}}</h1>
      <div v-if="isLoading">Loading...</div>

      <div v-else-if="showOrder">
        <OrderItem :items="itemsOrdered" :order-id="orderId" :total-price="totalPrice" />
        <div class="centered">
          <button  id="back-list" class="button" @click="handleBack">Back to product list</button>
        </div>
      </div>

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
          <button type="submit" id="submit-order" class="button">Place Order</button>
        </form>
      </div>

      <div v-if="isError" id="error_div">{{ error_message  }} </div>

  </main>
</template>

<script setup>
  import productService from '../services/productService'
  import orderService from '../services/orderService'
  import ProductList from './ProductList.vue'
  import OrderItem from './OrderItem.vue';
  import {onMounted, ref} from 'vue';

  const title = ref("Product list")
  const isLoading = ref(true);
  const failedLoading = ref(false)
  const productsData = ref([]);
  const categories = ref([]);

  const selected = ref([]);
  const customer_name = ref('');
  const itemsOrdered = ref([]);
  const totalPrice = ref(0);
  const orderId = ref('');
  const showOrder = ref(false);

  const isError = ref(false);
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
      error_message.value = "An unknown error has occured ("+error.message+")"
    }
    finally {
      isLoading.value = false;
    }

  })

  function handleBack() {
    showOrder.value = false;
    title.value = "Product list";
    selected.value = [];
  }

  async function setFilter(category) {
    if (category.trim() == "") {
      category = undefined
    }
    selected.value = [];
    try {
      const res = await productService.getAllProducts(category);
      productsData.value = res.data;
    }
    catch (error) {
      error_message.value = "An unknown error has occured ("+error.message+")"
      isError.value = true;
      failedLoading.value =true;
    }
  }

  async function handleOrder() {
    try {
      const res = await orderService.placeOrder(customer_name.value,selected.value);
      isError.value = false;
      const resData = res.data
      itemsOrdered.value = resData.items;
      totalPrice.value =resData.total_price;
      orderId.value = resData.order_id;
      showOrder.value =true;
      console.log(resData.items);
      title.value = "Order recap";
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
          error_message.value = "An unknown error has occured ("+error.message+")"
      }

      console.log(error.status)
      isError.value = true;
    }
  }
</script>

<style scoped>

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

  #order-form input[type=text],  .button{
    min-width: 200px;
    min-height: 50px;
    background-color: var(--color-background-soft);
    border: none;
    color: var(--color-text);
    font-size: large;
  }

  .button:hover {
    background-color: var(--color-background-mute);
    cursor: pointer;
  }

  #order-form div {
    margin-bottom: 15px;
  }

  .category-select{
    cursor: pointer;
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

</style>
