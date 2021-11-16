print("What is your bill amount ")
User_bill = float(input())
print("How many percent you want to tip")
User_tip_percentage = float(input())  
print("Number of peoples to split the bill with")
User_split_peoples = int(input())

Bill_Percent = User_tip_percentage * .1
Bill_With_Tip = Bill_Percent + User_bill
Final_Bill = Bill_With_Tip / User_split_peoples

print(f"Total Bill for {User_split_peoples} peoples is {Final_Bill} each")



