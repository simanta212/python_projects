print ("Your Weight 'in KGs'")
weight  = float(input())
print ("Enter your height 'in Meters'\nIf u wish to calculate in feet press 1 ")
height  = float(input())

bmi = float (weight)/(float(height*height))
if height == 1:
    print ("Enter your height in feet")
    converted_height = float(input())
    new_height_meter = float(converted_height/3.28)
    print ("Your height is \n"+str(new_height_meter)+" meters")
    
    converted_bmi = float(weight)/float(new_height_meter*new_height_meter)
    print("your bmi is \n"+ str(converted_bmi))


else:
    print ("your bmi is\n"+str(bmi))

# new_height_meter = float(converted_height/3.28 or height)
# converted_bmi = float(((weight)/float(new_height_meter*new_height_meter)) or bmi)

# if bmi or converted_bmi == 30:
#     print ("motey sarkar")
# elif bmi or converted_bmi < 18.5:
#     print ("lamkhutey sarkar")
# elif 18.5 <= bmi or converted_bmi >= 24.9:
#     print ("Fit sarkat")
# elif 25 <= bmi or converted_bmi >= 29.9:
#     print ("Gym jana paryo sarkar")
# else:
#     print ("Fit")



