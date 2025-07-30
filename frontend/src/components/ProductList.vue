<template>
    <div class="product_list">
        <h1>Product List</h1>

        <ul>
            <li v-for="product in items" :key="product.id">
                <ProductItem 
                :ProductId="product.id"
                :name="product.name"
                :category="product.category"
                :price="product.price"
                />
            </li>
        </ul>

    </div>

</template>

<script setup>
import ProductItem from './ProductItem.vue';
    defineProps({
        items : {
            type: Array,
            required: true
        }
    })
</script>

<style scoped>
    .product_list ul {
        list-style: none;
    }
    
</style>