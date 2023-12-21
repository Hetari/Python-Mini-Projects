from data import *
import os

# coins convertor to $
def total(quarter, dime, nickel, penny):
    quarter *= 0.25
    dime *= 0.10
    nickel *= 0.05
    penny *= 0.01
    return quarter + dime + nickel + penny


def available():
    global bool0
    global bool1
    global bool2
    bool0 = MENU[start]["ingredients"]["water"] < water
    bool1 = MENU[start]["ingredients"]["milk"] < milk
    bool2 = MENU[start]["ingredients"]["coffee"] < coffee
    return (bool0 and bool1 and bool2)


print("--------Welcome to Coffee Machine ---------")
clear_screen = 'cls' if os.name == 'nt' else 'clear'
while(True):
    start = input("What would you like? (espresso, latte, cappuccino) or to view the report (report): ") or 'report'

    if start == 'report':
        print(MENU[start])
        pass
    
    elif start == 'off':
        print("Turned off...")
        pass

    else:
        # check the recourses
        if available() == 0:
            os.system()
            if bool0 == 0:
                print("There is no enough water in the tank!")
                pass
            if bool1 == 0:
                print("There is no enough milk in the tank!")
                pass
            if bool2 == 0:
                print("There is no enough coffee in the tank!")
                pass
            break
        
        os.system('clear_screen')
        print("Please insert coins")
        quarters = eval(input("How many quarters?: "))
        dimes = eval(input("How many dimes?: "))
        nickels = eval(input("How many nickels?: "))
        pennies = eval(input("How many pennies?: "))
        
        total_money = total(quarters, dimes, nickels, pennies)
        
        water = (water - MENU[start]["ingredients"]["water"])
        milk = (milk - MENU[start]["ingredients"]["milk"])
        coffee = (coffee - MENU[start]["ingredients"]["coffee"])
        money = format((total_money - MENU[start]["ingredients"]["price"]), ".1f")
        
        os.system('clear_screen')
        print("Here is $" + money, "in change.")
        pass
    pass
