import random
random_integer = random.randint(1, 10)
print(random_integer)

#0.0000000 - 0.9999999....
random_float = random.random() * 5
print(random_float)
# random_float * 5
#0.000000 - 4.9999999..
love_score = random.randint(1, 100)
print(f"your love score is {love_score}")



# Write your code about flip coin👇
# Hint: Remember to import the random module first. 🎲
import random
random_side = random.randint(0, 1)
if random_side == 1:
  print ("Heads")
else:
  print("Tails")



states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

daca vrei sa scimbi un element din lista:
states_of_america[1] = "Pencilvania"

#daca vrei sa adaugi un element la lista:
states_of_america.append("Erikland")

#daca vrei sa adaugi o lista la lista:
states_of_america.extend(["Erikland", "Biancaland"])

#daca vrei sa adaugi un element intre alte doua elemente:
states_of_america.insert(2, "Erikland")

#daca vrei sa stergi un element din lista;
states_of_america.remove("Erikland")

print(states_of_america)




#cine va plati random:

names = names_string.split(", ")
import random
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

num_of_states = len (states_of_america)

print(states_of_america - 1)



fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][2]) #lista este aleasa de prima paranteza, pozitia este aleasa de a doua paranteza


#treasure map:

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "x"

print(f"{line1}\n{line2}\n{line3}")


