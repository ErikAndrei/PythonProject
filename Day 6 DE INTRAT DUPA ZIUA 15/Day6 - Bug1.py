#Defining Functions:

def my_function():
  print("Hello")
  print("Bye")

#Calling Functions:
my_function()



#Cod pentru a face robotelul sa sara peste obstacole:

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump_the_wall():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

jump_the_wall()
jump_the_wall()
jump_the_wall()
jump_the_wall()
jump_the_wall()
jump_the_wall()

#for loop: functie cand dorim sa facem o actiune de mai multe ori

for stem in range(6):
    jump_the_wall()


#while loop = functie care se repeta pana cand conditia este adevarata

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)


#Daca sfarsitul traseului este generat random folosim o negare a WHILE-ului:
while not at_goal():
    jump()



#Daca traseul este generat random (nu se stie unde trebuie sa sari si unde nu)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left() #am scos move() -ul pentru ca este in ultima linie de else si se lovea de zid
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#asta e codul propriu-zis:
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


#Traseu generat random + wall-uri fara limita de inaltime:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()