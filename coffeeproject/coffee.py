from data import MENU

Items = MENU
Items_espresso = Items["espresso"]
Items_latte = Items["latte"]
Items_cappuccino = Items["cappuccino"]
# print(Items["espresso"])



def rerun():
    order_false = True
    while order_false:
        user_choice = input("what do you want? \n'espresso','latte', 'cappuccino'?").lower()
        if user_choice == "off":
            print("out os service")
            exit()
        if user_choice == "espresso":
            print(Items_espresso["cost"])
            print("dollars")
            rerun()
        elif user_choice == "latte":
            print(Items_latte["cost"])   
            print("dollars")
            rerun()
        elif user_choice == "cappuccino":
            print(Items_cappuccino["cost"])
            print("dollars")
            rerun()
        
        else: 
            
            print ("please type correct name of the product")
            order_false = False
            rerun()
rerun()     