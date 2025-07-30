<template>
    <div>
        <ul>
            <li v-for="product in items" :key="product.id">
                <ProductItem 
                :name="product.name"
                :price="product.price"
                />
            </li>
        </ul>
        <div>
            <span>Total Price :</span>
            <span>{{ new Intl.NumberFormat("en-US", {style: "currency", currency:"USD"}).format(totalPrice) }}</span>
        </div>
        <div>
            <span>Order ID</span>
            <span>{{ orderId }}</span>
        </div>

    </div>
</template>

<script setup>
defineProps({
        items : {
            type: Array,
            required: true
        },
        totalPrice : Number,
        orderId : String
    })

</script>