run = True

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0.0
coins = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}


def sufficient_resources(coffee, available_resources):
    if coffee["ingredients"]["water"] <= available_resources["water"] and available_resources["milk"] >= \
            coffee["ingredients"]["milk"] and coffee["ingredients"]["coffee"] <= available_resources["coffee"]:
        return "ok"
    elif coffee["ingredients"]["water"] > available_resources["water"]:
        return "water"
    elif coffee["ingredients"]["milk"] > available_resources["milk"]:
        return "milk"
    else:
        return "coffee"


def calculate_value(input_coins):
    return input_coins["quarters"] * 0.25 + input_coins["dimes"] * 0.1 + input_coins["nickles"] * 0.05 + input_coins[
        'pennies'] * 0.01


while run:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "off":
        run = False
    elif prompt == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: \
        ${money}")
    elif prompt in MENU and sufficient_resources(MENU[prompt], resources) == "ok":
        print("Please insert coins.")
        coins["quarters"] = int(input("how many quarters?: "))
        coins["dimes"] = int(input("how many dimes?: "))
        coins["nickles"] = int(input("how many nickles?: "))
        coins["pennies"] = int(input("how many pennies?: "))
        if calculate_value(coins) < MENU[prompt]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            resources["water"] -= MENU[prompt]["ingredients"]["water"]
            resources["milk"] -= MENU[prompt]["ingredients"]["milk"]
            resources["coffee"] -= MENU[prompt]["ingredients"]["coffee"]
            money += MENU[prompt]["cost"]
            if calculate_value(coins) > MENU[prompt]["cost"]:
                print(f"Here is ${round(calculate_value(coins) - MENU[prompt]['cost'], 2)} in change.")
            print(f"Here is your {prompt}. Enjoy!")
    elif prompt in MENU:
        print(f"Sorry there is not enough {sufficient_resources(MENU[prompt], resources)}")
    else:
        exit(f"Unknown command {prompt}\nTerminating...")
