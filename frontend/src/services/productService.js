import axios from 'axios'

export default { getAllProducts(category) {
    if (category != undefined) {
        return axios.get("/api/products?category="+encodeURIComponent(category));
    }

    return axios.get("/api/products");
}
}