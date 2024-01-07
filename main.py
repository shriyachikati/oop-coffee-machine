from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

menu_items = menu.get_items().split("/")
menu_items.remove('')
print(menu_items)

def retrieve(item):
    item_name = item.name
    item_price = item.cost
    item_water = item.ingredients["water"]
    item_coffee = item.ingredients["coffee"]
    item_milk = item.ingredients["milk"]

    return item_name, item_price, item_water, item_coffee, item_milk

continue_serve = 'yes'

while continue_serve == 'yes':
    user_drink = input("What would you like to drink today? ")
    item = menu.find_drink(user_drink.lower())

    if item == None:
        if user_drink == 'report':
            coffee_maker.report()
            money_machine.report()
    elif item == 'off':
        break
    else:
        name, price, water, coffee, milk = retrieve(item)
        if coffee_maker.is_resource_sufficient(item):
            print(f"Please pay ${price}.")
            if money_machine.make_payment(price):
                coffee_maker.make_coffee(item)

    continue_serve = input("Would you like to have another drink?('yes' or 'no) ")


