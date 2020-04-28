class Funcs:
    def AskMenu(self):
        br = True
        in1, in2, in3, in4, in5, in7 = "", "", "", "", "", ""
        price, priceB, fryprice, P_ket = 0.00, 0.00, 0.00, 0.00
        sandoptions = {
            "chicken": 5.25,
            "beef": 6.25,
            "tofu": 5.75
        }
        bevoptions = {
            "small": 1.00,
            "medium": 1.75,
            "large": 2.25
        }
        fryoptions = {
            "small": 1.00,
            "medium": 1.50,
            "large": 2.00
        }
        while in7 != 'y' and in7 != 'n':
            in7 = input("Would you like a sandwhich?")
            if in7 == 'y':
                print("Your sandwhich options are,")
                print(list(sandoptions.keys()))
                in1 = input("What type of sandwhich would you like?")
                in1 = in1.lower()
                try:
                    price = sandoptions[in1]
                    br = False
                except KeyError:
                    print("That is not an option!")
            elif in7 != 'n' and in7 != 'y':
                print("That is not an option! Please input y or n.")
        print(price)
        while in2 != 'y' and in2 != 'n':
            in2 = input("Would you like a beverage? y/n")
            if in2 == 'y':
                print("Your beverage options are,")
                print(list(bevoptions.keys()))
                in3 = input("What size beverage would you like?")
                br1 = True
                in3 = in3.lower()
                try:
                    priceB = bevoptions[in3]
                    print("Price of beverage is ", priceB)
                except:
                    print("That is not an option!")
                    in2 = "Error"
            elif in2 != 'y' and in2 != 'n':
                print("Please input y or n.")
        while in4 != 'y' and in4 != 'n':
            in4 = input("Would you like french fries?")
            if in4 == 'y':
                fryprice = 1.00
                print("Your fry options are,")
                print(list(fryoptions.keys()))
                in5 = input("What size would you like?")
                in5 = in5.lower()
                in6 = ""
                while in6 != 'y' and in6 != 'n':
                    in6 = input("Would you like to mega size?")
                    if in6 == 'n':
                        fryprice = fryoptions[in5]
                    elif in6 == 'y':
                        fryprice = 2.00
                    else:
                        print('That is not an option!')
            elif in4 != 'y' and in4 != 'n':
                print("Please input y or n.")
        numketc = input("How many ketchup packets would you like?")
        P_ket = int(numketc) * 0.25
        return price + priceB + fryprice + P_ket - 1 if in2 == 'y' and in4 == 'y' else price + priceB + fryprice + P_ket
cont = True
FinalVals = []
while cont:
    a = Funcs()
    FinalVals.append(a.AskMenu())
    x = input("Would you like to place another order? y/n")
    if x == "y":
        cont = True
    elif x == "n":
        cont = False
    else:
        print("That is not an option, assuming yes.")
FLPrice = 0
for x in FinalVals:
    FLPrice = FLPrice + x
print("Total price is ", FLPrice)