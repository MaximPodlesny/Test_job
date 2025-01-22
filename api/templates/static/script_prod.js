const urlParams = new URLSearchParams(window.location.search);
const artikul = urlParams.get('artikul');

const API_URL = "https://localhost:8000/api/v1/products";

async function fetchProductData() {
try{
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({artikul: artikul})
    });
    if (response.ok) {
    const product_data = await response.json();
        
        const productDetailsDiv = document.getElementById('product-details');
        productDetailsDiv.innerHTML = `
            <h2>${product_data.name}</h2>
            <p><b>Артикул:</b> ${product_data.artikul}</p>
            <p><b>Цена:</b> ${product_data.price}</p>
            <p><b>Рейтинг:</b> ${product_data.rating}</p>
            <p><b>Количество:</b> ${product_data.total_quantity}</p>
        `;
    } else {
        document.getElementById('product-details').innerHTML = 'Ошибка при загрузке данных';
    }
}
    catch(error) {
        document.getElementById('product-details').innerHTML = 'Ошибка: ' + error;
    }
}
fetchProductData();