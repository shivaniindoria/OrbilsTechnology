function addToCart() {
    // Perform necessary actions to add the item to the cart

    // Change the class of the button to apply the new style
    document.getElementById("addToCartButton").classList.remove("btn-dark");
    document.getElementById("addToCartButton").classList.add("btn-outline-primary");
    document.getElementById("addToCartButton").innerText = "Added to Cart";

    // Optionally, disable the button to prevent multiple clicks
    document.getElementById("addToCartButton").disabled = true;

    document.getElementById("goToCartLink").classList.remove("d-none");

    // Optionally, display a notification message
    alert("Item has been added to your cart!");
  }
