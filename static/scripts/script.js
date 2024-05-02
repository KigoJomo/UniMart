document.addEventListener("DOMContentLoaded", function () {
  const filterBtn = document.getElementById("filter");
  const categoriesList = document.getElementById("categories");
  const productsContainer = document.getElementById("products");
  const categoryIndicator = document.getElementById("categoryIndicator");
  filterBtn.addEventListener("click", () => {
    categoriesList.classList.toggle("categoriesVisible");
  });

  function createProductElement(productName, price) {
    // Create elements
    const productDiv = document.createElement("div");
    const img = document.createElement("img");
    const descDiv = document.createElement("div");
    const descRow = document.createElement("div");
    const productNameHeader = document.createElement("h4");
    const pricePara = document.createElement("p");
    const addToCartButton = document.createElement("button");

    // Set attributes and classes
    productDiv.classList.add("product", "column");
    //   img.setAttribute("src", "{% static 'images/placeholder.jpg' %}");
    img.setAttribute("src", "static/images/placeholder.jpg");
    img.setAttribute("alt", "");
    descDiv.classList.add("desc", "column");
    descRow.classList.add("row");
    productNameHeader.textContent = productName;
    pricePara.textContent = `kes ${price}`;
    pricePara.classList.add("price");
    addToCartButton.textContent = "add to cart";

    // Construct structure
    descRow.appendChild(productNameHeader);
    descRow.appendChild(pricePara);
    descDiv.appendChild(descRow);
    descDiv.appendChild(addToCartButton);
    productDiv.appendChild(img);
    productDiv.appendChild(descDiv);

    return productDiv;
  }

  // Function to fetch products based on selected category
  function getProducts(category) {
    console.log(`Category: ${category}`);
    if (!category) {
      categoryIndicator.innerText = "All Products";
    } else {
      categoryIndicator.innerText = category;
    }
    fetch(`/products/${category}`)
      .then((response) => response.json())
      .then((data) => {
        // Clear current product list
        productsContainer.innerHTML = "";

        // Display products for the selected category
        data.forEach((product) => {
          const productName = product.name;
          const price = product.price;
          const productElement = createProductElement(productName, price);
          productsContainer.appendChild(productElement);
        });
      })
      .catch((error) => console.error("Error fetching products:", error));
  }

  getProducts();


  document
    .getElementById("All")
    .addEventListener("click", () => getProducts());
  document
    .getElementById("Electronics")
    .addEventListener("click", () => getProducts("Electronics"));
  document
    .getElementById("Clothing")
    .addEventListener("click", () => getProducts("Clothing"));
  document
    .getElementById("Home_and_Kitchen")
    .addEventListener("click", () => getProducts("Home and Kitchen"));
  document
    .getElementById("Books")
    .addEventListener("click", () => getProducts("Books"));
  document
    .getElementById("Health_and_Beauty")
    .addEventListener("click", () => getProducts("Health and Beauty"));
  document
    .getElementById("Toys_and_Games")
    .addEventListener("click", () => getProducts("Toys and Games"));
  document
    .getElementById("Sports_and_Outdoors")
    .addEventListener("click", () => getProducts("Sports and Outdoors"));
  document
    .getElementById("Automotive")
    .addEventListener("click", () => getProducts("Automotive"));
  document
    .getElementById("Grocery")
    .addEventListener("click", () => getProducts("Grocery"));
  document
    .getElementById("Office_Supplies")
        .addEventListener("click", () => getProducts("Office Supplies"));

    const searchBar = document.getElementById("searchBar");

    // Add event listener to the search form submission
    searchBar.addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent form submission

      const searchInput = document.getElementById("search").value;
      if (searchInput.trim() !== "") {
        searchProducts(searchInput);
      }
    });

    // Function to fetch products based on search query
    function searchProducts(query) {
      fetch(`/search/?query=${query}`)
        .then((response) => response.json())
        .then((data) => {
          // Clear current product list
            productsContainer.innerHTML = "";
            const response = document.createElement("p");
            response.classList.add("response");
            response.innerText = "Search results for " + query;
            productsContainer.appendChild(response);

          // Display products for the selected category
          data.forEach((product) => {
            const productName = product.name;
            const price = product.price;
            const productElement = createProductElement(productName, price);
            productsContainer.appendChild(productElement);
          });
        })
        .catch((error) => console.error("Error searching products:", error));
    }
});
