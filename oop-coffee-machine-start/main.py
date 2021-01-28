from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
    order = input(f"What would you like?({menu.get_items()}): ")
    if order == 'off':
        is_on = False
    if order == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
