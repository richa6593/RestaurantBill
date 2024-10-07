print(".....................Welcome to Harvest Table................\n")
print("Here's the menu :\n")
print("Pizza : Rs 450\nCoffee : Rs 200\nSandwich : Rs 250\nQuesedilla : Rs 550\n")

menu = {'Pizza': 450,'Coffee': 200,'Sandwich': 250,"Quesedilla": 550}

order_total=0

item_1=input("Enter your First item to order :")
if item_1 in menu:
    order_total=order_total +menu[item_1]
    print(f"Order of {item_1} has been recieved\n")

a=input("Do you want to order anything else?(Yes/No)\n")
if a=='Yes' or a=='YES' or a=="yes":
    item_2=input("\nEnter your next order :")
    if item_2 in menu:
        order_total=order_total + menu[item_2]
        print(f"Order of {item_2} has been recieved\n")
        print("\nThankyou for ordering !! \nThe total price to pay is :",order_total)
    
else:
  print("Sure,so the total price to pay is :",order_total)
