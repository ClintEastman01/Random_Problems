menu = {'pizza': 6, 'nachos': 6, 'cheeseburger': 10, 'coke': 5, 'water': 4}


def concession_food():
    current_order = []  # creates an empty array
    while True:
        order = input()  # takes the user input
        if order in menu:
            current_order.append(order)  # enter the user input into the array
        else:
            current_order.append('coke')  # enter coke in the array if the user chooses an option that is not on the menu
        if is_order_complete():
            return current_order


def is_order_complete():      # this function was used to stop the while true loop in the concession function
    print("Anything else? yes/no")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        raise Exception("invalid input")


def getTotal(prices):  # This function gets the total prices using the array to search the dictionary using the keys the user inputted into the array
    total_prices = 0
    for i in prices:
        x = menu.get(i)  # this line use the keys that was obtain from the array to ge the value in the dictionary
        total_prices += x   # this line takes each key it finds and adds it to a grand total
    return total_prices


def calc_Tax(sub):  # This function calculate all the taxes
    tax_per = 0.07
    tax = tax_per * sub
    total = sub + tax
    print('Your total is $' + str(total))


calc_Tax(getTotal(concession_food()))
