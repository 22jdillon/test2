"""This project will be a place where you can buy stuff from a supermarket. You can add items to your cart, view your cart, remove items, checkout, choose if you want to click and collect or have it home delivered, see how much money it costs in total."""

import sys
import os


food_choices = [["takis", 7], ["milk", 6], ["butter", 8], ["eggs", 10], ["cheese", 12], ["cereal", 8], ["chicken", 10], ["steak", 20]]
cart = []
addresses = []


def clear():
    """This clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    """This prints all options for home page."""
    print("1)Shop")
    print("2)View cart")
    print("3)Checkout")
    print("4)Exit")


def print_cart():
    """This prints the users cart in a nice table way, showing the name and price of the product."""
    clear()
    print("Products in cart:\n")
    print(f"{'   Food':<13} Price")
    print("____________________")
    number = 0
    for food, price in cart:
        number = number + 1
        print(f"{number}) {food:<10} ${price:.2f}")


def cart_options():
    """This shows all options that you can do in te view cart menu."""
    print("")
    print("1)remove item")
    print("2)continue shopping")


def remove():
    """This removes products from cart."""
    while True:
        clear()
        print_cart()
        try:
            remove = int(input("\nWhat product do you want to remove?\n> "))
            if remove > 0 and remove < (len(cart)+1):
                cart.pop(remove-1)
                break
            else:
                error_message()
        except ValueError:
            value_error_message()


def print_food():
    """This prints all foods the user can add to their cart as well as their price while displaying it in a table."""
    print(f"{'   Food':<13} Price")
    print("____________________")
    number = 0
    for food, price in food_choices:
        number = number + 1
        print(f"{number}) {food:<10} ${price:.2f} ")


def add():
    """This allows the user to add food to their cart."""
    while True:
        clear()
        print_food()
        print("")
        try:
            add = int(input("What product would you like add to your cart?\n> "))
            if add > 0 and add < (len(food_choices)+1):
                cart.append(food_choices[add-1])
                break
            else:
                error_message()
        except ValueError:
            value_error_message()


def checkout():
    """This shows users the possible options at the checkout menu."""
    print_cart()
    print("\n1) Contine shopping.")
    print("2) Checkout.")


def deliver():
    """This collects information about the user for when they select the deliver at checkouts."""
    clear()
    name = input("Please enter your first and last name:\n> ")
    clear()
    street = input("Please enter your street name:\n> ")
    clear()
    house_number = int(input("Please enter your house number:\n> "))
    clear()
    city = input("Enter your city:\n> ")
    clear()
    address = [name, street, house_number, city]
    return address


def click_and_collect(prompt="Please enter your phone number\n> "):
    """This collects information about the user for when they select the click and collect at checkouts."""
    while True:
        clear()
        name = input("What is your first and last name\n> ")
        clear()
        print(f"Is {name} correct?")
        print("1) yes")
        print("2) no")
        try:
            choice = int(input("> "))
            if choice == 1:
                user_name = name
                break
            elif choice == 2:
                print("")
            else:
                error_message()
        except ValueError:
            value_error_message()
    while True:
        try:
            clear()
            phone = int(input(prompt))
            if len(str(phone)) > 10:
                print("Invalid input, the phone number you have entered is more than 10 units long. Please try again.")
                input_continue()
            elif len(str(phone)) < 10:
                print("Invalid input, the phone number you have entered is less than 10 units long. Please try again.")
                input_continue()
            else:
                clear()
                total_cost = calculate_cost(cart)
                print(f"Thank you for shopping with us {user_name}!\nYou will be contacted threw your phone number ({phone}) when your order is ready for pickup and you will need to pay ${total_cost} when you arrive at the store.")
                sys.exit()
        except ValueError:
            value_error_message()


def delivery_or_pickup():
    """This shows the user the possible awnsers after they confurmed they want to checkout."""
    print("Would you rather want to pick up your order or have it delivered?\n")
    print("1) Click and Collect")
    print("2) Deliver")


def calculate_cost(user_cart):
    """This calculates the total amount all the products cost in the users cart and send returns it to 'total_cost'."""
    cost = 0
    for i in user_cart:
        cost = cost + i[1]  # this "i[i]" only takes the second value of the 2d list e.g. cheeze, 7 it will take the 7 and it to the cost. this will be repeted for all the products in the cart.
    return cost


def error_message():
    """This is a error message for when the user enters the right data type but wrong e.g. the possible inputs are 1 and 2, if the user enters 3 this error message wil be used."""
    print("\nInvalid input.")
    input("Press any button to contine\n> ")


def input_continue():
    """This is a contine button."""
    input("Press any button to contine\n> ")


def value_error_message():
    """This is a error message for when the user enters a wrong data type."""
    print("\nInvalid input. Please enter digits only.")
    input("Press any button to contine\n> ")


def main():
    """This is all of the code."""
    while True:
        clear()
        menu()
        try:
            choice = int(input("\nWhat would you like to do?\n> "))
            if choice == 1:
                clear()
                add()
            elif choice == 2:
                while True:
                    clear()
                    print_cart()
                    cart_options()
                    try:
                        choice = int(input("> "))
                        if choice == 1:
                            remove()
                        elif choice == 2:
                            print("")
                            break
                        else:
                            error_message()
                    except ValueError:
                        value_error_message()
            elif choice == 3:
                while True:
                    clear()
                    checkout()
                    try:
                        choice = int(input("> "))
                        if choice == 1:
                            break
                        elif choice == 2:
                            while True:
                                clear()
                                delivery_or_pickup()
                                try:
                                    choice = int(input("> "))
                                    if choice == 1:
                                        click_and_collect()
                                    elif choice == 2:
                                        while True:
                                            try:
                                                add_address = deliver()
                                                print(f"Hi {add_address[0]}! You are in {add_address[3]} and live in {add_address[2]} {add_address[1]}. \nIs all of this information correct?")
                                                print("\n1) Yes")
                                                print("2) No")
                                                choice = int(input("> "))
                                                if choice == 1:
                                                    addresses.append(add_address)
                                                    while True:
                                                        total_cost = calculate_cost(cart)
                                                        clear()
                                                        print(f"The total cost of all your products is ${total_cost}")
                                                        try:
                                                            user_bank = int(input("How much money do you have to pay for grocaries?\n> $"))
                                                            if user_bank < total_cost:
                                                                clear()
                                                                print("you do not have enough money to but these products!")
                                                                sys.exit()
                                                            else:
                                                                user_bank = user_bank - total_cost
                                                                clear()
                                                                print(f"Thank you for shopping with us! Your remaining balance is ${user_bank} and your products will be deliverd to {add_address[2]} {add_address[1]}!")
                                                                sys.exit()
                                                        except ValueError:
                                                            value_error_message()
                                                elif choice == 2:
                                                    print("")
                                                else:
                                                    error_message()
                                            except ValueError:
                                                value_error_message()
                                    else:
                                        error_message()
                                except ValueError:
                                    value_error_message()
                        else:
                            error_message()
                    except ValueError:
                        value_error_message()
            elif choice == 4:
                clear()
                print("Goodbye!")
                sys.exit()
            else:
                error_message()
        except ValueError:
            value_error_message()


main()
