print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = input("What percentage of tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
fbill = float(bill)
ftip = float(tip)
fpeople = float(people)
tip_amt = fbill * ( ftip / 100)
tot_bill = fbill + tip_amt
bill_pp = tot_bill / fpeople
final_amt = round(bill_pp, 2)
final_amt = "{:.2f}".format(bill_pp)
print(f"Each person should pay: ${final_amt}")
