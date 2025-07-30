<template>
    <div 
        class="product" 
        :class="{ selected: selected }" :id="`product-${productId}`"
        @click="$emit('select',productId)"
    >
        <h2>{{ name }}</h2>
        <div class="infos">
            <span>Category: {{ category }}</span>
            <span>{{ new Intl.NumberFormat("en-US", {style: "currency", currency:"USD"}).format(price) }}</span>
        </div>
    </div>
</template>

<script setup>
    const props = defineProps({
        productId : Number,
        name : String,
        category : String,
        price : Number,
        selected: {
            type: Boolean,
            default: false
        }
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
        transition: .05s ease-in;
        cursor: pointer;
    }

    .product:hover {
        background-color: var(--color-background-mute);
    }

    .product.selected {
        background-color: var(--color-background-mute-lighter);
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