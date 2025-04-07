import sys
import os


food_choices = [["takis", 7], ["milk", 6], ["butter", 8], ["eggs", 10], ["cheese", 12], ["cereal", 8], ["chicken", 10], ["steak", 20]]
cart = []
user = []
addresses = []


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    name = input("Please enter your first and last name:\n> ")
    street = input("Please enter your street name:\n> ")
    house_number = input("Please enter your house number:\n> ")
    city = input("Enter your city:\n> ")

    address = [name, street, house_number, city]
    return address

def user_details(prompt="Please enter your phone number\n> "):
    while True:
        name = input("What is your first and last name\n> ")
        print(f"Is {name} correct?")
        print("1) yes")
        print("2) no")
        choice = int(input("> "))
        if choice == 1:
            break
        if choice == 2:
            print("")

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

def error_message():
    print("\nInvalid number. Please enter digits only.")
    input("Press any button to contine\n> ")

def input_continue():
    input("\nPress any button to contine\n> ")

def main():
    while True:
        clear()
        menu()
        try:
            choice = int(input("\nWhat would you like to do?\n> "))
            if choice == 1:
                clear()
                add()
            elif choice == 2:
                clear()
                print_cart()
                input_continue()
            elif choice == 3:
                clear()
                clear()
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
                                user_details()
                                total_cost = calculate_cost(cart)
                                print(f"The total cost of all your products is ${total_cost}")
                                print("Thank you for shopping with us! You will be contacted when your products are ready to be picked up")
                            elif choice == 2:
                                while True:
                                    add_address = deliver()
                                    print(f"Hi {add_address[0]}! You are in {add_address[3]} and live in {add_address[2]} {add_address[1]}. \nIs all of this information correct?")
                                    print("\n1) Yes")
                                    print("2) No")
                                    choice = int(input("> "))
                                    if choice == 1:
                                        addresses.append(add_address)
                                        while True:
                                            total_cost = calculate_cost(cart)
                                            print(f"The total cost of all your products is ${total_cost}")
                                            user_bank = int(input("How much money do you have to pay for grocaries?"))
                                            if user_bank < total_cost:
                                                print("you do not have enough money to but these products!")
                                                break
                                            if user_bank >= total_cost:
                                                user_bank = user_bank - total_cost
                                                print(f"Thank you for shopping with us! Your remaining balance is ${user_bank}.")
                                                sys.exit()
                                    if choice == 2:
                                        print("")
                    else:
                        print("Please enter one of the corrosponding numbers")


            else:
                print("Please enter one of the corrosponding numbers")                            
        except ValueError:
            error_message()
                
                                

                            


     


main()
