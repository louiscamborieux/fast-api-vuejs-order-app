<template>
    <div class="order-recap">
        <div>
            Items
        </div>
        <ul>
            <li v-for="product in items">
                <span>{{product.name}}</span>
                <span>{{ new Intl.NumberFormat("en-US", {style: "currency", currency:"USD"}).format(product.price) }}</span>
            </li>
        </ul>
        <div>
            <span>Total Price : </span>
            <span>{{ new Intl.NumberFormat("en-US", {style: "currency", currency:"USD"}).format(totalPrice) }}</span>
        </div>
        <div>
            <span>Order ID: </span>
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

<style scoped> 
    .order-recap {
        font-size: larger;
    }

    li span {
        font-size: large;
    }

    .order-recap div {
        padding: 5px 5px;
    }

    .order-recap ul {
        padding-left: 15px;
    }

    .order-recap li {
        display: flex;
        justify-content: space-between;
    }
</style>