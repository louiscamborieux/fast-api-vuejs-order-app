<script setup>

import NavBar from './components/navBar.vue'

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


