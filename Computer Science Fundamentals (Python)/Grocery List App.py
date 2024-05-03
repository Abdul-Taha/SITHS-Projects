import datetime


Cart=['Meat','Cheese']
end = False




def remove_item():
    if len(Cart) == 0:
        print("\n\nYou have no items in your Cart")
    else:
        match = False
        items = ''
        resp = 'y'
        for i in range(len(sorted(Cart))):
            if i == 0:
                items+=Cart[i]
            else:
                items+=', '+Cart[i]
        while match == False and resp == 'y':
            print("\n\n"+items+"\n\n")
            item = str(input('What item would you like to remove? (Please Type exactly as Given Above): ')).replace(' ','')
            for i in range(len(Cart)):
                if item.lower() == Cart[i].replace(' ','').lower():
                    match = True
                    Cart.pop(i)
                    break
            if match == False:
                print("This item may not be in your Cart")
                resp = str(input("Would you like try again?(y/n): ")).replace(' ','').lower()
                while True:
                    if resp == 'y' or 'n':
                        break
                    else:
                        resp = str(input("That's not y or n. Try Again: ")).replace(' ','').lower()
        if(resp == 'n'):
            print("Unsuccessfully removed Item")
        else:
            print("Successfully removed Item")
           
def add_item():
    Cart.append(str(input("\n\nEnter an Item to add to your Cart: ")).capitalize())

while end == False:
    resp = str(input("\n\nWhat would you like to do?:\n\nShow Time|Enter t\nShow Cart|Enter s\nAdd Item|Enter a\nRemove Item|Enter r\nEnd Program|Enter e\n\n")).replace(' ','').lower()
    if resp == 's':
        items = ''
        for i in range(len(Cart)):
            if i == 0:
                items+=Cart[i]
            else:
                items+=', '+Cart[i]
        print("\n\n"+items)
    elif resp == 'a':
        add_item()
    elif resp == 'r':
        remove_item()
    elif resp == 'e':
        break
    elif resp == 't':
        print("\n\nIt is "+str(datetime.datetime.now()))
    else:
        print("\n\nThat's not an Option\n\n")
print("\n\nThank you for using Abdul's Shopping App")


