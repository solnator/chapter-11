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
        losse = int(input(f"Enter the numbers of losses for {team_name}: "))
        team[team_name] = [win, losse]
    except ValueError:
        print("Enter a valid number.")

## (a) Calculate and display winning percentage.
team_to_check = input("\nEnter a team name to see its winning percentage: ")
if team_to_check in team:
    win, losse = team[team_to_check]
    total_games = win + losse
    if total_games > 0:
        winning_percentage = (win / total_games) * 100
        print(f"{team_to_check}'s winning percentage:{winning_percentage:.2f}%")
    else:
        print(f"{team_to_check} has not played any games.")
else:
    print(f"{team_to_check} is not in the records.")

# (b) Create a list of the number of wins for each team
wins_list = [record[0] for record in team.values()]
print("\nList of number of wins for each team:", wins_list)

# (c) Create a list of teams with winning records
winning_teams = [team for team, record in team.items() if record[0] > record[1]]
print("Teams with winning records:", winning_teams)


### Exercise 6        By ChatGPT

teams = {}

while True:
    game_input = input(
        "Enter game scores (e.g., 'Team1 10-7 Team2') or 'done' to finish: "
    )
    if game_input.lower() == "done":
        break

    try:
        parts = game_input.split("-")
        team1_data = parts[0].strip().rsplit(" ", 1)  # Split into team name and score
        team2_data = parts[1].strip().split(" ", 1)  # Split into score and team name

        team1, score1 = team1_data[0], int(team1_data[1])
        team2, score2 = team2_data[1], int(team2_data[0])

        if team1 not in teams:
            teams[team1] = [0, 0]
        if team2 not in teams:
            teams[team2] = [0, 0]

        # Update wins and losses based on scores
        if score1 > score2:
            teams[team1][0] += 1
            teams[team2][1] += 1
        elif score2 > score1:
            teams[team2][0] += 1
            teams[team1][1] += 1
        else:
            print("It's a tie! No wins or losses recorded.")

    except (ValueError, IndexError):
        print("Invalid input format. Please try again.")

print("\nTeam Records (wins, losses):")
for team, record in teams.items():
    print(f"{team}: {record}")

### Question 9
from random import shuffle

deck = [
    {"value": i, "suit": c}
    for c in ["spade", "clubs", "diamond", "hearts"]
    for i in range(2, 15)
]
shuffle(deck)

for i in range(2):
    print(deck[i]["value"], deck[i]["suit"])

hand = deck[:2]


def is_flush(cards):
    suits = [card["suit"] for card in cards]
    return len(set(suits)) == 1


def is_kind(cards):
    values = [card["value"] for card in cards]
    return len(set(values)) == 1


# print("Hand:", hand)
if is_flush(hand):
    print("The three cards form a flush!")
else:
    print("The three cards do not form a flush.")

if is_kind(hand):
    print("The three cards form a kind.")
else:
    print("The three cards do not form a kind.")


### Question 11
def is_valid_cipher(word, encoded):
    word = input("Enter a string: ")
    encoded = input(f"Enter a {len(word)} encoded letter: ")
    word = word.lower()
    encoded = encoded.lower()
    if len(word) != len(encoded):
        return False
    mapping = {}
    reverse_mapping = {}
    for o, e in zip(word, encoded):
        if o in mapping:
            if mapping[o] != e:
                return False
    else:
        if e in reverse_mapping:
            return False
        mapping[o] = e
        reverse_mapping[e] = o

    return True


print(is_valid_cipher("BOOK", "CXYZ"))
print(is_valid_cipher("BOOK", "CXXK"))
print(is_valid_cipher("BOOK", "CXXZ"))
