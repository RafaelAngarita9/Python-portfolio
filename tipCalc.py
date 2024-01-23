print("Welcome to the tip calculator")
total = float(input("What was the total bill?"))
numberPeople = int(input("How many people will split the bill?"))
tip = int(input("What percentage tip would you like to give?10,12 or 15?"))

tipPercentage = tip / 100
billTotal = total + (total*tipPercentage)
perPersonTotal = billTotal / numberPeople
perPersonTotalRounded = "{:.2f}".format(perPersonTotal)
print(f"Each person should pay: {perPersonTotalRounded}")

