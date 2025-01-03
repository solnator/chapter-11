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


### Question 4
users = {
    "user1": "Pass@1234",
    "user2": "Secure!5678",
    "user3": "Alpha$9012",
    "user4": "Beta#3456",
    "user5": "Gamma%7890",
    "user6": "Delta^1234",
    "user7": "Epsilon&5678",
    "user8": "Zeta*9012",
    "user9": "Theta(3456",
    "user10": "Iota)7890",
}
while True:
    username = input("Enter your username: ")

    if username in users:
        correct_password = users[username]
        password = input("Enter your password: ")
        if password == correct_password:
            print("You are now logged in to the system.")
            break
        else:
            print("Password is invalid!")
    else:
        print("You are no't valid user to the system.")


### Question 5
team = {}

while True:
    team_name = input("Enter the team name: ")
    if team_name.lower() == "done":
        break
    try:
        win = int(input(f"Enter the numbers of wins for {team_name}: "))
        losse = int(input(f"HEnter the numbers of losses for {team_name}: "))
        team[team_name] = [win, losse]
    except ValueError:
        print("Enter a valid number.")

## (a) Calculate and display winning percentage.
team_to_check=input('\nEnter a team name to see its winning percentage: ')
if team_to_check in team:
    win,losse=team[team_to_check]
    total_games =win +losse
    if total_games>0:
        winning_percentage=(win/total_games)*100
        print(f'{team_to_check}\'s winning percentage:{winning_percentage:.2f}%')
    else:
        print(f'{team_to_check} has not played any games.')
else:
    print(f'{team_to_check} is not in the records.')
    