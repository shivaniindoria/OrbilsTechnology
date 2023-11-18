function fetchQuote() {
    fetch('/api/quote/')
    .then(response => response.json())
    .then(data => {
        document.getElementById('Quote-text').textContent = data.content;
    })
    .catch(error => console.error('Error:', error));
}
window.onload = fetchQuote;

function fetchFunFact() {
    fetch('/api/fun-fact/')
    .then(response => response.json())
    .then(data => {
        document.getElementById('fun-fact-text').textContent = data.text;
    })
    .catch(error => console.error('Error:', error));
}
window.onload = fetchFunFact;

// -------------------cart-apis---------------------------

// function loadCart() {
//     fetch('/api/cart/')
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('cart-item-view').textContent = data.datas;
//     })
//     .catch(error => console.error('Error:', error));
// }
// window.onload = fetchFunFact;
// function fetchFunFact() {
//     fetch('/api/fun-fact/')
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('fun-fact-text').textContent = data.text;
//     })
//     .catch(error => console.error('Error:', error));
// }
// window.onload = fetchFunFact;