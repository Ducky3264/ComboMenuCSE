{"changed":true,"filter":false,"title":"test.py","tooltip":"/test.py","value":"\nin1, in2, in3, in4, in5 = \"\", \"\", \"\", \"\", \"\"\nprice, priceB, fryprice, P_ket = 0.00, 0.00, 0.00, 0.00\nsandoptions = {\n    \"chicken\": 5.25,\n    \"beef\": 6.25,\n    \"tofu\": 5.75\n}\nbevoptions = {\n    \"small\": 1.00,\n    \"medium\": 1.75,\n    \"large\": 2.25\n}\nfryoptions = {\n    \"small\": 1.00,\n    \"medium\": 1.50,\n    \"large\": 2.00\n}\ncont = True\nbr = True\nwhile br:\n    print(\"Your sandwhich options are,\")\n    print(list(sandoptions.keys()))\n    in1 = input(\"What type of sandwhich would you like?\")\n    in1 = in1.lower()\n    try:\n        price = sandoptions[in1]\n        br = False\n    except KeyError:\n        print(\"That is not an option!\")\n    \nprint(price)\nwhile in2 != 'y' and in2 != 'n':\n    in2 = input(\"Would you like a beverage? y/n\")\n    if in2 == 'y':\n        print(\"Your beverage options are,\")\n        print(list(bevoptions.keys()))\n        in3 = input(\"What size beverage would you like?\")\n        br1 = True\n    \n        in3 = in3.lower()\n        try:\n            priceB = bevoptions[in3]\n            print(\"Price of beverage is \", priceB)\n        except:\n            print(\"That is not an option!\")\n            in2 = \"Error\"\n       \n    elif in2 != 'y' and in2 != 'n':\n        print(\"Please input y or n.\")\n\nwhile in4 != 'y' and in4 != 'n':\n    in4 = input(\"Would you like french fries?\")\n    if in4 == 'y':\n        fryprice = 1.00\n        print(\"Your fry options are,\")\n        print(list(fryoptions.keys()))\n        in5 = input(\"What size would you like?\")\n        in5 = in5.lower()\n        in6 = input(\"Would you like to mega size?\")\n        if in6 == 'n':\n            fryprice = fryoptions[in5]\n        else:\n            fryprice = 2.00\n    elif in4 != 'y' and in4 != 'n':\n        print(\"Please input y or n.\")\nnumketc = input(\"How many ketchup packets would you like?\")\nP_ket = int(numketc) * 0.25\nbev_add = \"a \" + in3 + \" sized beverage, \" if in3 != \"\" else \"\";\nfry_add = \" a \" + in5 + \" sized fry, \" if in5 != \"\" else \"\";\nket_add = \" and \" + str(numketc) + \" ketchup packets.\"\nprint(\"Your final order is a \" + in1 + \" sandwhich, \" + bev_add + fry_add + ket_add)\nfinal_price = price + priceB + fryprice + P_ket - 1 if in2 == 'y' and in4 == 'y' else price + priceB + fryprice + P_ket\nprint(\"Total price is \", final_price)","undoManager":{"mark":-20,"position":100,"stack":[[{"start":{"row":24,"column":10},"end":{"row":24,"column":12},"action":"insert","lines":["\"\""],"id":978}],[{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["Y"],"id":979},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["o"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["u"]}],[{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":[" "],"id":980},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["h"]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["a"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["v"]},{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"insert","lines":[" "],"id":981},{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"insert","lines":["a"]}],[{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"insert","lines":[" "],"id":982},{"start":{"row":24,"column":22},"end":{"row":24,"column":23},"action":"insert","lines":["s"]},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["p"]},{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"remove","lines":["e"],"id":983},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"remove","lines":["p"]},{"start":{"row":24,"column":22},"end":{"row":24,"column":23},"action":"remove","lines":["s"]},{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"remove","lines":[" "]},{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"remove","lines":["a"]},{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"remove","lines":[" "]},{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"remove","lines":["e"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"remove","lines":["v"]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"remove","lines":["a"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"remove","lines":["h"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"remove","lines":[" "]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"remove","lines":["u"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"remove","lines":["o"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"remove","lines":["Y"]}],[{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["T"],"id":984},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["h"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["a"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":[" "],"id":985},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["i"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"insert","lines":[" "],"id":986},{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"insert","lines":["n"]},{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"insert","lines":["o"]},{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"insert","lines":["t"]}],[{"start":{"row":24,"column":22},"end":{"row":24,"column":23},"action":"insert","lines":[" "],"id":987},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["a"]},{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"insert","lines":[" "],"id":988},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["o"]},{"start":{"row":24,"column":27},"end":{"row":24,"column":28},"action":"insert","lines":["p"]},{"start":{"row":24,"column":28},"end":{"row":24,"column":29},"action":"insert","lines":["t"]},{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"insert","lines":["i"]},{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["o"]},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["N"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":["!"]},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"insert","lines":["\\"]}],[{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"remove","lines":["\\"],"id":989},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"remove","lines":["!"]},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"remove","lines":["N"]}],[{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["n"],"id":990},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":["!"]}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":991}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["b"],"id":992},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"insert","lines":["o"]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"insert","lines":["o"]},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":["l"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":[" "],"id":993},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["b"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["r"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["e"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["a"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["k"]},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["e"]},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["r"]}],[{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":[" "],"id":994},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":[" "],"id":995},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["t"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["r"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["u"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"remove","lines":["e"],"id":996},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"remove","lines":["u"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"remove","lines":["r"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"remove","lines":["t"]}],[{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["f"],"id":997},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["a"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["l"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["s"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"remove","lines":["e"],"id":998},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"remove","lines":["s"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"remove","lines":["l"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"remove","lines":["a"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"remove","lines":["f"]}],[{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["f"],"id":999},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["a"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["l"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["s"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["e"],"id":1000},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["a"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["n"]}],[{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["n"],"id":1001},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"remove","lines":["a"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"remove","lines":["e"]}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"remove","lines":["r"],"id":1002},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"remove","lines":["e"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"remove","lines":["k"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"remove","lines":["a"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"remove","lines":["e"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"remove","lines":[" "],"id":1003},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"remove","lines":["l"]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"remove","lines":["o"]},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"remove","lines":["o"]},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":["b"]},{"start":{"row":16,"column":1},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":1},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":1004}],[{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"remove","lines":["f"],"id":1005}],[{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["F"],"id":1006}],[{"start":{"row":17,"column":10},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":1007},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["w"]},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["h"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["i"]},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":["l"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":[" "],"id":1008},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["!"]},{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["b"]},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["r"]}],[{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":[" "],"id":1009}],[{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"remove","lines":[" "],"id":1010}],[{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":[":"],"id":1011}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "],"id":1012}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "],"id":1013}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "],"id":1014}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "],"id":1015}],[{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"remove","lines":["!"],"id":1016}],[{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"remove","lines":["e"],"id":1017},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"remove","lines":["s"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"remove","lines":["l"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["a"]},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"remove","lines":["F"]}],[{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["T"],"id":1018},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["r"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["u"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "],"id":1019}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":8},"action":"insert","lines":["    "],"id":1020}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "],"id":1021}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":8},"action":"insert","lines":["    "],"id":1022}],[{"start":{"row":26,"column":39},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":1023},{"start":{"row":27,"column":0},"end":{"row":27,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":8},"action":"remove","lines":["    "],"id":1024}],[{"start":{"row":24,"column":32},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":1025},{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"insert","lines":["        "]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["b"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["r"]}],[{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":[" "],"id":1026},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["="]}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":[" "],"id":1027},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["F"]},{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["a"]},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["l"]},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["s"]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":8},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":1028},{"start":{"row":37,"column":0},"end":{"row":37,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"insert","lines":["b"],"id":1029},{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"insert","lines":["r"]},{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"insert","lines":["1"]}],[{"start":{"row":36,"column":11},"end":{"row":36,"column":12},"action":"insert","lines":[" "],"id":1030},{"start":{"row":36,"column":12},"end":{"row":36,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"insert","lines":[" "],"id":1031},{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":["T"]},{"start":{"row":36,"column":15},"end":{"row":36,"column":16},"action":"insert","lines":["r"]},{"start":{"row":36,"column":16},"end":{"row":36,"column":17},"action":"insert","lines":["u"]},{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":18},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":1032},{"start":{"row":37,"column":0},"end":{"row":37,"column":8},"action":"insert","lines":["        "]},{"start":{"row":37,"column":8},"end":{"row":38,"column":0},"action":"insert","lines":["",""]},{"start":{"row":38,"column":0},"end":{"row":38,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":8},"action":"remove","lines":["    "],"id":1033},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "]},{"start":{"row":37,"column":8},"end":{"row":38,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["t"],"id":1041},{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":["r"]},{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":["y"]}],[{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"insert","lines":[" "],"id":1042}],[{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"remove","lines":[" "],"id":1043},{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"remove","lines":["y"]},{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"remove","lines":["r"]},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"remove","lines":["t"]},{"start":{"row":37,"column":4},"end":{"row":37,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":39,"column":8},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":1044},{"start":{"row":40,"column":0},"end":{"row":40,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["t"],"id":1045},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["r"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"insert","lines":["y"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":[":"]}],[{"start":{"row":40,"column":8},"end":{"row":40,"column":12},"action":"insert","lines":["    "],"id":1046}],[{"start":{"row":40,"column":36},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":1047},{"start":{"row":41,"column":0},"end":{"row":41,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":41,"column":8},"end":{"row":41,"column":12},"action":"remove","lines":["    "],"id":1048}],[{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["e"],"id":1049},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["x"]},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["c"]},{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":["e"]},{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"insert","lines":["p"]},{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"insert","lines":["t"]},{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":[":"]}],[{"start":{"row":41,"column":15},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":1050},{"start":{"row":42,"column":0},"end":{"row":42,"column":12},"action":"insert","lines":["            "]},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["p"]},{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":["r"]}],[{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"insert","lines":["i"],"id":1051},{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"insert","lines":["n"]},{"start":{"row":42,"column":16},"end":{"row":42,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":42,"column":17},"end":{"row":42,"column":19},"action":"insert","lines":["()"],"id":1052}],[{"start":{"row":42,"column":18},"end":{"row":42,"column":20},"action":"insert","lines":["\"\""],"id":1053}],[{"start":{"row":42,"column":19},"end":{"row":42,"column":20},"action":"insert","lines":["T"],"id":1054},{"start":{"row":42,"column":20},"end":{"row":42,"column":21},"action":"insert","lines":["h"]},{"start":{"row":42,"column":21},"end":{"row":42,"column":22},"action":"insert","lines":["a"]},{"start":{"row":42,"column":22},"end":{"row":42,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":42,"column":23},"end":{"row":42,"column":24},"action":"insert","lines":[" "],"id":1055},{"start":{"row":42,"column":24},"end":{"row":42,"column":25},"action":"insert","lines":["i"]},{"start":{"row":42,"column":25},"end":{"row":42,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":42,"column":26},"end":{"row":42,"column":27},"action":"insert","lines":[" "],"id":1056},{"start":{"row":42,"column":27},"end":{"row":42,"column":28},"action":"insert","lines":["n"]},{"start":{"row":42,"column":28},"end":{"row":42,"column":29},"action":"insert","lines":["o"]},{"start":{"row":42,"column":29},"end":{"row":42,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":42,"column":30},"end":{"row":42,"column":31},"action":"insert","lines":[" "],"id":1057},{"start":{"row":42,"column":31},"end":{"row":42,"column":32},"action":"insert","lines":["a"]},{"start":{"row":42,"column":32},"end":{"row":42,"column":33},"action":"insert","lines":["n"]}],[{"start":{"row":42,"column":33},"end":{"row":42,"column":34},"action":"insert","lines":[" "],"id":1058},{"start":{"row":42,"column":34},"end":{"row":42,"column":35},"action":"insert","lines":["o"]},{"start":{"row":42,"column":35},"end":{"row":42,"column":36},"action":"insert","lines":["p"]},{"start":{"row":42,"column":36},"end":{"row":42,"column":37},"action":"insert","lines":["t"]},{"start":{"row":42,"column":37},"end":{"row":42,"column":38},"action":"insert","lines":["i"]},{"start":{"row":42,"column":38},"end":{"row":42,"column":39},"action":"insert","lines":["o"]},{"start":{"row":42,"column":39},"end":{"row":42,"column":40},"action":"insert","lines":["n"]},{"start":{"row":42,"column":40},"end":{"row":42,"column":41},"action":"insert","lines":["!"]}],[{"start":{"row":42,"column":43},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":1059},{"start":{"row":43,"column":0},"end":{"row":43,"column":12},"action":"insert","lines":["            "]},{"start":{"row":43,"column":12},"end":{"row":43,"column":13},"action":"insert","lines":["i"]},{"start":{"row":43,"column":13},"end":{"row":43,"column":14},"action":"insert","lines":["n"]},{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"insert","lines":["2"]}],[{"start":{"row":43,"column":15},"end":{"row":43,"column":16},"action":"insert","lines":[" "],"id":1060},{"start":{"row":43,"column":16},"end":{"row":43,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":43,"column":17},"end":{"row":43,"column":18},"action":"insert","lines":[" "],"id":1061}],[{"start":{"row":43,"column":18},"end":{"row":43,"column":20},"action":"insert","lines":["\"\""],"id":1062}],[{"start":{"row":43,"column":19},"end":{"row":43,"column":20},"action":"insert","lines":["E"],"id":1063},{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":["r"]},{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"insert","lines":["r"]},{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"insert","lines":["o"]},{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"insert","lines":["r"]}],[{"start":{"row":44,"column":7},"end":{"row":44,"column":46},"action":"remove","lines":[" print(\"Price of beverage is \", priceB)"],"id":1064}],[{"start":{"row":40,"column":36},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":1065},{"start":{"row":41,"column":0},"end":{"row":41,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":41,"column":12},"end":{"row":41,"column":51},"action":"insert","lines":[" print(\"Price of beverage is \", priceB)"],"id":1066}],[{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"remove","lines":[" "],"id":1067}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":1069}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["o"],"id":1070},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["d"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["e"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":1071},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["="]}],[{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":[" "],"id":1072}],[{"start":{"row":0,"column":9},"end":{"row":0,"column":11},"action":"insert","lines":["[]"],"id":1073}],[{"start":{"row":0,"column":9},"end":{"row":0,"column":11},"action":"remove","lines":["[]"],"id":1074},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"remove","lines":[" "]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"remove","lines":["="]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"remove","lines":[" "]}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"remove","lines":["s"],"id":1075},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"remove","lines":["r"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"remove","lines":["e"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":["d"]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":["r"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["o"]}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":1076}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["i"],"id":1077},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["n"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["t"]},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":["e"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["r"]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["a"]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["t"]},{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["i"]},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["o"]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["n"]},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"remove","lines":["s"],"id":1078},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"remove","lines":["n"]},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"remove","lines":["o"]},{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"remove","lines":["i"]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"remove","lines":["t"]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"remove","lines":["a"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"remove","lines":["r"]},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"remove","lines":["e"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"remove","lines":["t"]},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"remove","lines":["n"]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"remove","lines":["i"],"id":1079}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["c"],"id":1080},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["o"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["n"]},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":[" "],"id":1081},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["="]}],[{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":[" "],"id":1082},{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"remove","lines":["t"],"id":1083}],[{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["T"],"id":1084},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["r"]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["i"]}],[{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"remove","lines":["i"],"id":1085}],[{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["u"],"id":1086},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":180,"scrollleft":0,"selection":{"start":{"row":20,"column":0},"end":{"row":20,"column":0},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"state":"start","mode":"ace/mode/python"}},"timestamp":1586271992153}