<template>
    <div class="orders-list">
        <h1>
            Orders
        </h1>
        <div v-if="isLoading">Loading...</div>

        <div v-else-if="!isError">
            <ul>
                <li v-for="order in orderData">
                    <OrderItem :items="order.items" :orderId="order.order_id" :totalPrice="order.total_price" />
                </li>
            </ul>
        </div>

        <div v-else id="error_div">{{ errorMessage  }} </div>
    </div>
</template>

<script setup>
import orderService from '@/services/orderService';
import {onMounted, ref} from 'vue';
import OrderItem from './OrderItem.vue';

const isLoading = ref(true);
const isError = ref(false);
const errorMessage =ref('');
const orderData = ref([]);

onMounted(async () => {
    try {
            const res = await orderService.getAllOrders();
            orderData.value = res.data;
    }
    catch (error) {
        isError.value = true;
        errorMessage.value = "Error while fetching last orders (code "+error.status+")"
    }
    finally {
        isLoading.value = false;
    }
})

</script>

<style scoped>

.orders-list ul {
    list-style-type: none;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
}

@media (max-width: 900px) {
    .orders-list ul {
        grid-template-columns: 1fr; /* ou repeat(1, 1fr) */
    }
}

.orders-list li {
    background-color: var(--color-background-soft);
    padding: 20px;
    border-radius: 15px;
}

.orders-list {
    padding: 45px;
}

.orders-list h1 {
    text-align: center;
    font-size: 45px;
}


</style>