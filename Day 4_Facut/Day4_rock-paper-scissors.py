rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#Incercarea mea:

my_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Sissors.\n"))
if my_move >2 or my_move <0:
  print("You typed an invalid number, you lose!")
else:
  print("You chose:")
  if my_move == 0:
    print(rock)
  elif my_move == 1:
    print(paper)
  else:
    print(scissors)
    
  import random
  print("PC chose:")
  random_move = random.randint(0, 2)
  if random_move == 0:
    print(rock)
  elif random_move == 1:
    print(paper)
  else:
    print(scissors)
  
  if my_move == 0 and random_move == 2:
    print("You win!")
  elif my_move ==1 and random_move == 0:
    print("You win!")
  elif my_move ==2 and random_move == 1:
    print("You win!")
  elif my_move ==0 and random_move == 0:
    print("It's a draw!")
  elif my_move ==1 and random_move == 1:
    print("It's a draw!")
  elif my_move ==2 and random_move == 2:
    print("It's a draw!")
  else:
    print("You lose!")




#Modelul facut in curs
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")