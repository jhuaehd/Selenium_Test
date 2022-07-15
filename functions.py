
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

