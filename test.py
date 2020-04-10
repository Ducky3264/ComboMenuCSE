class Funcs:



    def AskMenu(self):
        br = True
        in1, in2, in3, in4, in5 = "", "", "", "", ""
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


        while br:
            print("Your sandwhich options are,")
            print(list(sandoptions.keys()))
            in1 = input("What type of sandwhich would you like?")
            in1 = in1.lower()
            try:
                price = sandoptions[in1]
                br = False
            except KeyError:
                print("That is not an option!")

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
                in6 = input("Would you like to mega size?")
                if in6 == 'n':
                    fryprice = fryoptions[in5]
                else:
                    fryprice = 2.00
            elif in4 != 'y' and in4 != 'n':
                print("Please input y or n.")
        numketc = input("How many ketchup packets would you like?")
        P_ket = int(numketc) * 0.25

cont = True
while cont:
    a = Funcs()
    a.AskMenu()

bev_add = "a " + in3 + " sized beverage, " if in3 != "" else "";
fry_add = " a " + in5 + " sized fry, " if in5 != "" else "";
ket_add = " and " + str(numketc) + " ketchup packets."
print("Your final order is a " + in1 + " sandwhich, " + bev_add + fry_add + ket_add)
final_price = price + priceB + fryprice + P_ket - 1 if in2 == 'y' and in4 == 'y' else price + priceB + fryprice + P_ket
print("Total price is ", final_price)