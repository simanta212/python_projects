dict = {"ram":98, "sim":44, "chim":65}

grade = {}

for key in dict:
    # print(key)
    score = dict[key]
    if score > 90:
        grade[key] = "padantey"
        
    else:
        grade[key] = "fail"
    
print(grade)