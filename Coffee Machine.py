MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

PENNY = 0.01
NICKEL = 0.05
DIME = 0.1
QUARTER = 0.25

def change(quar,dim,nick,penn,cos):
    return quar*QUARTER + dim*DIME + nick*NICKEL + penn*PENNY - cos

def use_resource(resource,key,coffee):
    if key in MENU[coffee]["ingredients"]:
        resource[key] -= MENU[coffee]["ingredients"][key]
        return resource[key]
    else:
        MENU[coffee]["ingredients"][key] = 0

def machine():
    start = True
    while start:
        user = input("What would you like? (espresso/latte/cappuccino): ")

        if user == "report":
            for key in resources:
                print(f"{key} : {resources[key]}")

        elif user in MENU:
            print("Please input the coins")
            quarters = int(input("how many quarters? : "))
            dimes = int(input("how many dimes? : "))
            nickels = int(input("how many nickels? : "))
            pennies = int(input("how many pennies? : "))
            change_f = float(change(quarters,dimes,nickels,pennies,MENU[user]["cost"]))

            if change_f >= 0:
                print(f"Here is ${change_f}in change.")
                for keys in resources:
                    use_resource(resources,keys,user)
                print("Here is your latte ☕️. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("Please choose coffee in the list, Try again")

machine()
