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
    print("Products in cart:")
    print(f"{'   Food':<13} Price")
    print("____________________")
    number = 0
    for food, price in cart:
        number = number + 1
        print(f"{number}) {food:<10} ${price:.2f}")

def cart_option():
    print("1)remove item")
    print("2)checkout")

def remove():
    print_cart()
    remove = int(input("What product do you want to remove?\n> "))
    cart.pop(remove-1)

def checkout():
    print("Cart")



print_cart()
remove()
print_cart()