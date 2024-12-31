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


### Question 2 integrated to Question 1
## Find the products less than my money(find affordable products)
while True:
    try:
        money = input(
            "Enter an amount of money to find affordable products (or type 'done' to quit): "
        )
        if money.lower() == "done":
            break
        money = float(money)

        # Find products that are less than or equal to the entered amount
        affordable_products = [
            product for product, price in products.items() if price <= money
        ]

        if affordable_products:
            print("Products you can afford:")
            for product in affordable_products:
                print(f"- {product} (${products[product]:.2f})")
        else:
            print("No products are within your budget.")
    except ValueError:
        print("Please enter a valid amount.")


### Question 3 A and B
months = {}
while True:
    month_name = input("Enter month name(type ,done, when finish): ")
    if month_name.lower() == "done":
        break
    try:
        days = input(f"Enter the days of {month_name}: ")
        months[month_name] = days
    except ValueError:
        print("Enter a valid numbers.")
        
months = sorted(months)  ### Question B
print(months)
