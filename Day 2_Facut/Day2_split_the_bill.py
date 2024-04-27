#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# print("Welcome to the bill and tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 15, or 20? "))
# people_split = int(input("How many people to split the bill? "))
# final_tips = float(round(((bill * (tip/100) + bill))/people_split, 3))
# final_split = "{:.2f}".format(final_tips)   
# print(f"Each persons should pay: ${final_tips}")

#se foloseste "{:.2f}".format() ca sa iti arate zeroul de dupa virgula EX: 33.60

#sau
print("Welcome to the bill and tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 15, or 20? "))

people_split = int(input("How many people to split the bill? "))

total_as_percent = tip / 100

total_tip_amound = bill * total_as_percent

total_bill = bill + total_tip_amound

bill_per_person = total_bill / people_split

final_amount = round(bill_per_person, 2)

final_amount = "{:.2f}".format(bill_per_person)

print(f"Each persons should pay: ${final_amount}")