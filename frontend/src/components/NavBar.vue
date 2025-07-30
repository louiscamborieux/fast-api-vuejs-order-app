<template>
    <div id="navbar">
        <div class="link">
            <router-link class="route-link" to="/products">Products</router-link>
        </div>
        <div class="link">
            <router-link class="route-link" to="/orders">Orders</router-link>
        </div>
    </div>
</template>

<style scoped>
    #navbar{
        display: flex;
        align-items: center;
        padding: 5px;

        height: 60px;
        background-color: var(--color-background-soft);
        width: 100%;
        padding: 0;
    }

    .route-link {
        display: flex;

        align-items: center;
        justify-content: center;

        width: 100%;
        height: 40px;

        color: var(--color-text);
        background-color: var(--color-background-mute);
    }

    .route-link:hover {
        background-color: var(--color-background-mute-lighter);
    }

    #navbar .link {
        margin-left: 5px;
        margin-right: 5px;

    }

    .link {
        min-width: 80px;
    }

</style>