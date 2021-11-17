year = int(input("what year is it\n"))

if year/4==0 or year/100==0 or year/400:
    print(f"yea, year {year} is leap year")
else:
    print(f"No {year} is not leap year")