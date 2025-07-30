<template>
    <div class="product" :id ="`product-${productId}`">
        <h2>{{ name }}</h2>
        <div class="infos">
            <span>Category: {{ category }}</span>
            <span>{{ new Intl.NumberFormat("en-US", {style: "currency", currency:"USD"}).format(price) }}</span>
        </div>
    </div>
</template>

<script setup>
    defineProps({
        productId : Number,
        name : String,
        category : String,
        price : Number
    })
</script>

<style scoped>
    .product {
        border-radius: 8px;
        border-style: solid;
        border-color: var(--vt-c-indigo);
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 10px;
        padding-right: 10px;
        background-color: var(--color-background-soft);
        margin: 5px;
    }

    .product h2 {
        font-weight: bold;
        margin-bottom: clamp(10px,1vh,30px);
    }
    .product .infos {
        display: flex;
        justify-content: space-between;
    }

    .product .infos * {
        font-size: large;
    }
</style>