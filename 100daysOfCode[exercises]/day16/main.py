from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    if coffee=='latte':
        MoneyMachine().make_payment(Menu().menu[0].cost)
        CoffeeMaker().make_coffee()






    elif coffee=='espresso':
            MoneyMachine().make_payment(Menu().menu[1].cost)
            CoffeeMaker().make_coffee(Menu().menu[2].name)
    elif coffee=='cappuccino':
        MoneyMachine().make_payment(Menu().menu[2].cost)
        CoffeeMaker().make_coffee(Menu().menu[2].name)

     
        print('Insufficient cash')

while True:
    coffee=str(input("What would you like?(latte/espresso/cappuccino): ")).lower()

    if coffee=="report":
        CoffeeMaker().report()
        MoneyMachine().report()

    elif coffee=="menu":
        men=Menu().get_items().split("/")
        obj1=Menu().menu[0]
        obj2=Menu().menu[1]
        obj3=Menu().menu[2]
        print(f'{men[0]} : {obj1.cost}')
        print(f'{men[1]} : {obj2.cost}')
        print(f'{men[2]} : {obj3.cost}')
        

    elif coffee=="espresso" or coffee=='latte' or coffee=='cappuccino':
        main()
        
        
    else:
        Menu().find_drink(coffee)
        print('Transfering funds')
        print('Turning OFF coffee machine')
        break


    
