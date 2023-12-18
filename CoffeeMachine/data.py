water = 300
milk = 200
coffee = 100
money = 0

MENU = {
    "report": f"The coffee machine has:\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}gm\nMoney: ${money}",
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": None,
            "price": 1.50
        }
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
            "price": 2.50
        }
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
            "price": 3.00
        }
    }
}
