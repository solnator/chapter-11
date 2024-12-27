#### Exercise 11.5
### Question 1
## Suplayers form
products = {}
while True:
    product_name = input("Enter a product name (type done to quit): ")
    if product_name.lower() == "done":
        break
    try:
        product_price = float(input(f"Enter the price for {product_name}: "))
        products[product_name] = product_price
    except ValueError:
        print("Please enter avalid price.")

# Cnsumers form
while True:
    search_product = input(
        "Enter name of product to show the \
price of product(type done to quite): "
    )
    if search_product.lower() == "done":
        break
    if search_product in products:
        print(f"The price of {search_product} is $ {products[search_product]:.2f}")
    else:
        print(f"{search_product} is not available in the store.")

