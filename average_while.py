

lst = []
user_input = int(input())
lst.append(user_input)
sum = 0
while user_input != 0:
    user_input = int(input())
    lst.append(user_input)
else:
    for l in lst:
        sum += l
    average = sum / len(lst)
    print(len(lst))
    print(int(average))
