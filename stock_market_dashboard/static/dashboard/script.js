// Fetch stock data from the Django backend
async function fetchStocks() {
    const response = await fetch('/dashboard/');  // Update to fetch from the dashboard view
    const stocks = await response.json();
    const stockList = document.getElementById('stock-list');
    stockList.innerHTML = '';

    stocks.forEach(stock => {
        const stockItem = document.createElement('div');
        stockItem.className = 'border-b p-2';
        stockItem.innerHTML = `<strong>${stock.name}</strong> (${stock.symbol}): $${stock.price}`;
        stockList.appendChild(stockItem);
    });
}

// Call the fetchStocks function on page load
window.onload = fetchStocks;
