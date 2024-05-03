Coffees = {"Latte":3.50,"Mocha":2.75}
price = 0
resp = "null"
print("Welcome to my Coffee Shop!")


while True and resp != 'n':
    resp = "null"
    [print(i) for i in Coffees.keys()]
    order = str(input("What Coffee would you like to order?: ")).replace(' ','').lower()
    if order in [i.lower() for i in Coffees.keys()]:
        price+=Coffees[order.capitalize()]
        print("You owe "+str(price))
        while True and resp != 'n':
            resp = input("Would you like anything else? y/n: ").replace(' ','').lower()
            if resp == 'n':
                print("Good Bye!")
                break
            elif resp == 'y':
                break


            while resp != 'y':
                resp = input("Unrecongnized Input, Would you like to try Again? y/n: ").replace(' ','').lower()
                if resp == "n":
                    print("Good Bye!")
                    break
    else:
        while resp != 'y':
            resp = input("Unrecongnized Input, Would you like to try Again? y/n: ").replace(' ','').lower()
            if resp == "n":
                    print("Good Bye!")
                    break



