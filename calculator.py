from ast import operator
import math



def addition(num1, num2):
    sum = num1 + num2
    return sum

def difference(num1, num2):
    diff = num1 - num2
    return diff

def product(num1, num2):
    prod = num1 * num2
    return prod

def quotient(num1, num2):
    quot = num1/num2
    return quot
def exponential(num1, num2):
    expo = num1 ** num2
    return expo
def modulo(num1, num2):
    rem = num1 % num2
    return rem


num1 = float(input())
oper = ['+', '-', '*', '/', '**', '%']
user_operator = input()
num2 = float(input())

# ADDITION
if user_operator == oper[0]:
    print("{} + {} = {:,.2f}".format(num1, num2, addition(num1, num2)))
# SUBTRACTION
elif user_operator == oper[1]:
    print("{} - {} = {:,.2f}".format(num1, num2, difference(num1, num2)))
# MULTIPLICATION
elif user_operator == oper[2]:
    print("{} * {} = {:,.2f}".format(num1, num2, product(num1, num2)))
# DIVISION
elif user_operator == oper[3]:
    if num2 != 0:
        print("{} / {} = {:,.2f}".format(num1, num2, quotient(num1, num2)))
    else:
        print("Undefine, You can't devide number with zero.")
# POWER
elif user_operator == oper[4]:
    print("{} ** {} = {:,.2f}".format(num1, num2, exponential(num1, num2)))
# REMAINDER 
elif user_operator == oper[5]:
    if num2 != 0:
        print("{} % {} = {:,.0f}".format(num1, num2, modulo(num1, num2)))
    else:
        print("Undefine, You can't divide a number with zero.")
else:
    print("Invalid operator")