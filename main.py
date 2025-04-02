user = []
food_choices = [["takis", 7], ["milk", 6], ["butter", 8], ["eggs", 10], ["cheese", 12], ["cereal", 8], ["chicken", 10], ["steak", 20]]
cart = [["beans", 2], ["toast", 7]]

def menu():
    print("1)Shop")
    print("2)View cart")
    print("3)Checkout")
    print("4)Exit")

def stock():
    print("1)Add product")
    print("2)Back")

def print_cart():
    print("Products in cart:\n")
    print(f"{'   Food':<13} Price")
    print("____________________")
    number = 0
    for food, price in cart:
        number = number + 1
        print(f"{number}) {food:<10} ${price:.2f}")

def cart_options():
    print("1)remove item")
    print("2)checkout")

def remove():
    print_cart()
    remove = int(input("What product do you want to remove?\n> "))
    if remove > 0 and remove < (len(cart)+1):
        cart.pop(remove-1)
    else:
        print("Invalid input. Please try again.")

def print_food():
    print(f"{'   Food':<13} Price")
    print("____________________")
    number = 0
    for food, price in food_choices:
        number = number + 1
        print(f"{number}) {food:<10} ${price:.2f} ")

def add():
    print_food()
    add = int(input("What product would you like add to your cart?\n> "))
    if add > 0 and add < (len(food_choices)+1):
        cart.append(food_choices[add-1])
    else:
        print("Invalid input. Please try again.")

def checkout():
    print_cart()
    print("\n1) Contine shopping.")
    print("2) Checkout.")
    choice = int(input("> "))
    if choice == 1:
        print("")
    if choice == 2:
        print("still working")

def user_info():
    print("1) Click an collect.") 
    print("2) Home delivery.")
    choice = int(input("> "))
    if choice == 

user_info()