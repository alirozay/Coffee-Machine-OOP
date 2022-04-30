from money_machine import MoneyMachine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
end = False
while not end:
    items = menu.get_items()
    items = items[:len(items) - 1] + "?"
    choice = input("What would you like? " + items + ": ")
    if choice != 'report' and choice != 'off':
        item = menu.find_drink(choice)
        if item is not None:
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        end = True

if __name__ == '__main__':
    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
