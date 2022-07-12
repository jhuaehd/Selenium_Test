import math
import random

    

names = ['Cardo', 'JDC', 'Goku', 'Naruto', 'Luffy', 'Inuyasha', 'Kuroko', 'Rukawa']
name = random.choice(names)

print("List of Names: \n", names)

life = 7
while life > 0:
    user_input = input()
    guess_name = user_input[0].capitalize() + user_input[1:]
    if guess_name == name:
        print("Awesome!! You guess the name")
    else:
        life = life - 1
        print("Not the correct name")
        print("Life: ",life)
else:
    print("Better luck next time.")
    



