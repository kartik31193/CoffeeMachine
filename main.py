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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO 1: print resource report


def report():
    print(resources)

# TODO 2: check resource sufficient or not
def res_sufficiency(s):
    print("so you want: "+s)
    c=0
    for r in resources:
        if r in MENU[s]["ingredients"]:
            if resources[r]>=MENU[s]["ingredients"][r]:
                c+=1
        else:
            c+=1

    if c==3:
        cost=MENU[s]["cost"]
        print("your total is: "+str(cost)+"\n please insert coins." )
        print("quarters ?")
        q=int(input())
        print("dimes ?")
        d = int(input())
        print("nickles ?")
        n = int(input())
        print("pennies ?")
        p = int(input())
        total = process_coins(q, d, n, p)
        success(int(cost), total, s)
    else:
        print("Sorry we don't have that now")




# TODO 3: process coins

def process_coins(q,d,n,p):
    total=0.25*q+0.1*d+0.05*n+0.01*p
    return total



# TODO 4: check transaction successful or not


def success(cost,total,s):
    if total == cost:
        print("success...here is your order")
        make_coffee(s,profit,cost)

    if total<cost:
        print("Sorry that's not enough money. Money refunded.")

    if total>cost:
        print("success...here is your order and")
        print("Here is "+str(total-cost)+" dollars in change")
        make_coffee(s,profit,cost)

# TODO 5: make coffee
def make_coffee(s,profit,total):
    for r in resources:
        if r in MENU[s]["ingredients"]:
            resources[r] -= MENU[s]["ingredients"][r]
    profit+=total
    print("resources left: ")
    report()
    print(f"profit earned : ${profit}")

# TODO :main
is_on = True

while is_on:
    print("what do you like(espresso/latte/cappuccino): ")
    like = input()
    if like=="off":
        is_on=False
    if like=="report":
        report()
    if like=="espresso" or like=="latte" or like=="cappuccino":
        res_sufficiency(like)