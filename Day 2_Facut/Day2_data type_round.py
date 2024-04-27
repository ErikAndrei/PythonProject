#Data Types

#String
#str()
# print("Hello"[4])
# print("123"+"234")

#Integer
#int()
# print(123+345)
# 123_456_789

#Float
#float()
# 3.14159

#Boolean
# True
# False

# print(type(num_char)) = arata tipul de date (int, str, float

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has" + new_num_char + "characters." )

# a = float(123)
# print(type(a))
# print(70 + float("100.5"))
# print(str(70)+str(100))

#codul de mai jos face suna a doua cifre introduse la alegere Ex: 12 = 3; 39=12
# two_digit_number = input()
# first_digit=int(two_digit_number[0])
# second_digit=int(two_digit_number[1])
# two_digit_number=first_digit+second_digit
# print(two_digit_number)

#PEMDASLR
#() = paranteze
# ** = ridicare la putere ex: 2**3
# * = inmultire ex: 3*2
# / = impartire ex: 6/3
# + = adunare ex: 3+5
# - = scadere ex: 7-4

#calcul de BMI
#'int'il aproximeaza fara mai faca ce e dupa virgula; 'float' pune si ce e dupa virgula - linia 5
# height = input()
# weight = input()
# bmi_weight = int(weight)
# bmi_height = float(height)
# bmi = int(bmi_weight/(bmi_height**2)) 
# print(bmi)

#Rotunjire
#round()
#print(round(8/3))

#Scurtaturi
# score = 0
# score = score + 1 sau score += 1
# print(score)

#f-String
# score = 0
# height = 1.8
# isWinning = True
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#cate saptamani mai ai pana la 90 ani
# age = input()
# year = 90 - int(age)
# weeks = 52 * int(year)
# print(f"You have {weeks} weeks left.")