<template>
    <div class="product_list">
        <ul>
            <li v-for="product in items" :key="product.id">
                <ProductItem 
                :productId="product.id"
                :name="product.name"
                :category="product.category"
                :price="product.price"
                :selected="selected.includes(product.id)"
                @select="toggleSelection"
                />
            </li>
        </ul>

    </div>
</template>

<script setup>
import ProductItem from './ProductItem.vue';

const {items, selected } = defineProps({
    items : {
        type: Array,
        required: true
    },
    selected: {
        type: Array,
        required: true
    }
})

const emit = defineEmits(['update:selected'])

function toggleSelection(productId) {
    let newSelected
    if (selected.includes(productId)) {
        newSelected = selected.filter(id => id !== productId)
    } else {
        newSelected = [...selected, productId]
    }
    emit('update:selected', newSelected)
}
</script>

<style scoped>
    .product_list {
        width: 85vw;
        max-width: 2000px;
        min-width: 450px;
        margin-bottom: 30px;
    }

    .product_list ul {
        list-style: none;
        width: 100%
    }

</style>