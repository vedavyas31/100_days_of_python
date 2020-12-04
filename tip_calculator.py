print("Welcome to the tip calculator.")

bill = float (input("what was the total bill? "))
tip_percent = int (input("what percentage tip would you like to give? 10, 12, or 15? "))
people_count = int (input("How many people to split the bill? "))

tip = bill * (tip_percent / 100)
total_bill = bill + tip
split_bill = round(total_bill / people_count, 2)

print("Each person should pay {}".format(split_bill))
