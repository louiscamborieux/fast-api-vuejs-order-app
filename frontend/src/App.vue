<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import productService from './services/productService'
import orderService from './services/orderService'
import axios from 'axios'

import {onMounted, ref} from 'vue'

const data = ref(null);

onMounted(async () => {
  const res = await productService.getAllProducts();

  console.log(res);

  const res2 = await productService.getAllProducts("electronics");
  console.log(res2)

  const res3 = await orderService.placeOrder("test",[1,2]);
  console.log(res2)

})
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
  </main>
</template>

<style scoped>
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
