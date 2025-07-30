import axios from 'axios'

export default { placeOrder(customer_name, ids) {
    if (!Array.isArray(ids)) {
        return null;
    }

    return axios.post("/api/order",{
        customer_name : customer_name,
        product_ids : ids
    });
}
}