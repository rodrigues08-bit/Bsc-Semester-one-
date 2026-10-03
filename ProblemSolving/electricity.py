def bill(units):
    if units <= 100:
        return units * 5  #each unit costs 5/-
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7 #each unit above 100 costs 7/-
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10 #each unit above 200 costs 10/-


units = int(input("Enter units: "))

print("Electricity Bill =", bill(units))