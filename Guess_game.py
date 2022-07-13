import random
import time
    
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')

names = ['Cardo', 'JDC', 'Goku', 'Naruto', 'Luffy', 'Inuyasha', 'Kuroko', 'Rukawa']
name = random.choice(names)

print("List of Names :")

for i in range(len(names)):
    print(names[i], end=" ")


life = 7
t = 5
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
