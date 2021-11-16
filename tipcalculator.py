print("What is your bill amount ")
User_bill = float(input())
print("How many percent you want to tip")
User_tip_percentage = float(input())  
print("Number of peoples to split the bill with")
User_split_peoples = int(input())

Bill_Percent = User_tip_percentage * .1
Bill_With_Tip = Bill_Percent + User_bill
Total_Bill_Per_person = Bill_With_Tip / User_split_peoples
Final_Bill = round(Total_Bill_Per_person, 2)


print(f"Total Bill for {User_split_peoples} peoples is {Final_Bill} each")



