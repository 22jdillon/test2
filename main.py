food_choices = [["takis", 7], ["milk", 6], ["butter", 8], ["eggs", 10], ["cheese", 12], ["cereal", 8], ["chicken", 10], ["steak", 20]]
cart = []
user = []
addresses = []




def menu():
    print("")
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
    print("")
    add = int(input("What product would you like add to your cart?\n> "))
    if add > 0 and add < (len(food_choices)+1):
        cart.append(food_choices[add-1])
    else:
        print("Invalid input. Please try again.")

def checkout():
    print_cart()
    print("\n1) Contine shopping.")
    print("2) Checkout.")

def user_info():
    print("1) Click and collect.") 
    print("2) Home delivery.")
    choice = int(input("> "))
    if choice == 1:
        print("click and collect")

def deliver():
    name = input("Please enter your first and last name\n> ")
    street = input("Please eneter your streets name\n> ")
    house_number = input("Please enter your house number\n> ")
    city = input("Enter your city\n> ")

    address = [name, street, house_number, city]
    addresses.append(address)

def phone(prompt="Please enter your phone number\n> "):
    while True:
        try:
            phone = int(input(prompt))
            if len(str(phone)) > 10:
                print("Invalid input, the phone number you have entered is more than 10 units long. Please try again.")
            elif len(str(phone)) < 10:
                print("Invalid input, the phone number you have entered is less than 10 units long. Please try again.")
            else:
                print("checkout")
        except ValueError:
            print("Invalid number. Please enter digits only.")

def delivery_or_pickup():
    print("Would you rather want to pick up your order or have it delivered?\n")
    print("1) Click and Collect")
    print("2) Deliver")

def calculate_cost(user_cart):
    cost = 0
    for i in user_cart:
        cost = cost + i[1]
    return cost




def main():
    while True:
        menu()
        choice = int(input("\nWhat would you like to do?\n> "))
        if choice == 1:
            add()
        elif choice == 2:
            print_cart()
        elif choice == 3:
            checkout()
            while True:
                choice = int(input("> "))
                if choice == 1:
                    break
                elif choice == 2:
                    while True:
                        delivery_or_pickup()
                        choice = int(input("> "))
                        if choice == 1:
                            print("Click and Collect")
                        elif choice == 2:
                            deliver()
                            



main()

total_cost = calculate_cost(cart)
print(f"The total cost of all your products is ${total_cost}")