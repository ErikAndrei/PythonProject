# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride in the rollercoaster!")
# else:
#   print("Sorry, you have to grow taller before you can ride")

# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == equal to
# != not equal to


#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder.
# number = int(input())
# if number % 2 == 0:
#  print ("This is an even number.")
# else:
#  print("This is an odd number.")


# if = conditie primara
# elif = conditie secundara
# else = conditie finala

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride in the rollercoaster!")
#   age = int(input("what is your age? "))
#   if age <= 12:
#     print("Please pay $5.")
#   elif age <= 18:
#     print("Please pay $7.")
#   else:
#     print("Please pay $12.")
# else:
#   print("Sorry, you have to grow taller before you can ride")


#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Equal to or over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.


# height = float(input())
# weight = int(input())
# bmi = float(weight/(height**2))

# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 18.5:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")


#How to finder a leap year
# % = devided by

# year = int(input())
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")



#exercise:

# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#   print("You can ride in the rollercoaster!")
#   age = int(input("what is your age? "))
#   if age <= 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
#   wants_photo = input("Do you want a photo taken? Yes or No. ")
#   if wants_photo == "Yes":
#     bill += 3       #bill = bill + 3
    
#   print(f"Your final bills is ${bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride")




# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N

# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill +=20 
# else:
#   bill += 25
# if add_pepperoni == "Y":
#   if size == "S":
#      bill += 2
#   else:
#     bill += 3
# if extra_cheese == "Y":
#   bill += 1
# print(f"Your final bill is: ${bill}.")



# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#   print("You can ride in the rollercoaster!")
#   age = int(input("what is your age? "))
#   if age <= 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
  
#   elif age >= 45 and age <= 55:
#     print("Everything is going be ok. Have a ride on us!")
  
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
#   wants_photo = input("Do you want a photo taken? Yes or No. ")
#   if wants_photo == "Yes":
#     bill += 3
#   print(f"Your final bills is ${bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride")




#You are going to write a program that tests the compatibility between two people.

# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# combined_name = name1 + name2
# lower_names = combined_name.lower()
# t = lower_names.count('t')
# r = lower_names.count('r')
# u = lower_names.count('u')
# e = lower_names.count('e')
# first_digit = t + r + u + e

# l = lower_names.count('l')
# o = lower_names.count('o')
# v = lower_names.count('v')
# e = lower_names.count('e')
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score<10) or (score>90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")