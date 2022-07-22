

user_input = int(input())
fact = user_input
while user_input >= 2:
    user_input -= 1
    fact *= user_input
print("{:,.0f}".format(fact))