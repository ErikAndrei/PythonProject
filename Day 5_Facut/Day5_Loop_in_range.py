#Loops

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)


# Input a Python list of student heights

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print (f'total height = {total_height}')  

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print (f'number of students = {number_of_students}') 

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")


# Input a list of student scores

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print (f"The highest score in the class is: {highest_score}")


#For Loop in Range
for number in range(1, 11, 3):
  print(number)


#Gaus sum
total = 0
for number in range(1, 101):
  total += number
print(total)



target = int(input()) # Enter a number between 0 and 1000
even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number 
print(even_sum)

# or

alternative_sum = 0
for number in range(1, target + 1):
  if number % 2 == 0:
    alternative_sum += number
print(alternative_sum)


# Exercise
target = 100
for number in range(1, target + 1):
  target +=number
  if number % 3 == 0 and number %5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)




