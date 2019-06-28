"@author everydaycodings"
# A Program Which Simulates A Resturant

import time
import sys

print(" welcome to max restaurant ".upper().center(150, "="))

menu = ["sandwich", "burger", "kfc chicken", "pizza"]
toppings = ["onion", "cheese", "extra cheese", "chillies", "mushroom", "green papers",
            "tomato sauce", "chili sauce",
            "tomato ketchup", "chili ketchup", "french fries", "chips"]
item = input("what do you want to order:")

if item in menu:
    print("do you want your", item,
          "plan or you want to customize it with toppings? plane/customize")
    while True:
        user = input("what do you say:")
        if user == "plane":
            print("your order is in process")
            time.sleep(4.8)
            print("your order is ready enjoy your", item)
            break
        elif user == "customize":
            while True:
                user_1 = input("select your topping:")
                if user_1 in toppings:
                    print(user_1, "selected")
                elif user_1 == "not anymore":
                    print("your customized", item, "is getting ready")
                    time.sleep(4.8)
                    print("enjoy your", item)
                    sys.exit()
                elif item not in toppings:
                    print(user_1, "is not "
                    "available please select another topping")
        else:
            print("we couldn't understand "
                  "what did you said can you repeat it again")
            continue
else:
    print("Sorry,we dont sell", item, "in our restaurant")
