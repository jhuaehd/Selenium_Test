
# ====== VOWEL COUNT ========
# def vowel_count(s):
#     """Counts the number of vowels in s and returns the same
#     Ignores case of letters"""
#     VOWELS = "aeiouAEIOU"
#     vc = 0
#     for ch in s:
#         if ch in VOWELS:
#             vc += 1
#     return vc

# s = input()
# print(vowel_count(s))

# <======= ARGS NON-KEYWORD ARGUMENTS ========>
# def myFun(*argv):
#     for arg in argv:
#         print(arg)
 
 
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# ======= KWARGS KEYWORD ARGUMENTS ==========
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s = %s" % (key, value))

# myFun(first='Geeks', mid='for', last='Geeks', extension='Sr.')

# ========= DOCUMENT STRING ============
# def evenOdd(x):
#     'THIS FUNCTION IDENTIFIES IF A NUMBER IS EVEN OR ODD'
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")
 
 
# # Driver code to call the function
# print(evenOdd.__doc__)
# evenOdd(2)


# ====== RETURN STATEMENT ==========
# def square_value(num):
#     """This function returns the square
#     value of the entered number"""
#     return num**2
 
 
# print(square_value(2))
# print(square_value(-4))

# ====== FUNCTION PASS BY REFERENCE ========
# def myFun(x):
#     x[0] = 20
 
 
# # Driver Code (Note that lst is modified
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)


# ======== BROKEN FUNCTION =======
# def myFun(x):
 
#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#     x = [20, 30, 40]
 
 
# # Driver Code (Note that lst is not modified
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)

# arr = [1, 2, 3, 4, 5, 6, 7]

# sum = 0
# for num in arr:
#     sum += num
# print(sum)

# number = 5105

# if number % 3 == 0:
#     print("Divisible by 3")
# elif number % 5 == 0:
#     print("Divisible by 5")
# else:
#     print(number)

# ========= MULTIPLICATION TABLE ==============

# def multiplicationTable(column, row):
#     for r in range(1, row + 1):
#         print("\n", r, end="\t")
#         for c in range(2, column + 1):
#             print(c*r, end="\t")


# column = int(input("Column: "))
# row = int(input("Row: "))
# multiplicationTable(column, row)



# ============ DICE SIMULATOR (TEXT BASED)================
import random

user1 = input("Player 1: ")
user2 = input("Player 2: ")

# dice values
dice_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# rocker, paper, scissor for the first attempt
p = ['rock', 'paper', 'scissor']

while True:
    winner = None
    player1 = random.choice(p)
    player2 = random.choice(p)
    print(user1 + ": " + player1 + "  " + user2 + ": " + player1)
    if player1 != player2:
        print(user1 + ":" + player1  + "<---->"+ user2 + ":" + player2)
        if player1 == 'rock' and player2 == 'paper':
            winner = user2
            print("Winner:",winner,"\n")
        elif player1 == 'rock' and player2 == 'scissor':
            winner = user1
            print("Winner:",winner,"\n")
        elif player1 == 'paper' and player2 == 'rock':
            winner = user1
            print("Winner:",winner,"\n")
        elif player1 == 'paper' and player2 == 'scissor':
            winner = user2
            print("Winner:",winner,"\n")
        elif player1 == 'scissor' and player2 == 'rock':
            winner = user2
            print("Winner:",winner,"\n")
        elif player1 == 'scissor' and player2 == 'paper':
            winner = user1
            print("Winner:",winner,"\n")
        break

print("{} wins, {} will start first\n".format(winner[0].capitalize() + winner[1:], winner[0].capitalize() + winner[1:]))

player1_score = 0
player2_score = 0

game  = True

if winner == user2:
    while game:
        print("Please press enter to roll the dice")
        enter = input("Player 2 turn _")
        if player2_score < 100:
            player2_dice = random.choice(dice_value)
            player2_score += player2_dice
            print("Player 1({}): ".format(user1) + str(player1_score) + "\n" +"Player 2({}): ".format(user2) + str(player2_score) + "(+{})".format(player2_dice) + "\n")
        else:
            print("Congrats " + user2)  
            game = False

        print("Please press enter to roll the dice")
        enter = input("Player 1 turn _")
        
        if player1_score < 100:
            player1_dice = random.choice(dice_value)
            player1_score += player1_dice
            print("Player 1({}): ".format(user1) + str(player1_score)  + "(+{})".format(player1_dice) + "\n" +"Player 2({}): ".format(user2) + str(player2_score) + "\n")
        else:
            print("Congrats " + user1)
            game = False
    else:
        print("===================")
        print("    Nice Game    ")
else:
    while game:
        print("Please press enter to roll the dice")
        enter = input("Player 1 turn _")
        
        if player1_score < 100:
            player1_dice = random.choice(dice_value)
            player1_score += player1_dice
            print("Player 1({}): ".format(user1) + str(player1_score)  + "(+{})".format(player1_dice) + "\n" +"Player 2({}): ".format(user2) + str(player2_score) + "\n")
        else:
            print("Congrats " + user1)
            game = False

        print("Please press enter to roll the dice")
        enter = input("Player 2 turn _")
        if player2_score < 100:
            player2_dice = random.choice(dice_value)
            player2_score += player2_dice
            print("Player 1({}): ".format(user1) + str(player1_score) + "\n" +"Player 2({}): ".format(user2) + str(player2_score) + "(+{})".format(player2_dice) + "\n")
        else:
            print("Congrats " + user2)  
            game = False
    else:
        print("===================")
        print("    Nice Game    ")
