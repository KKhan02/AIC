# Write a Python program which accepts the radius of a circle from the user and compute the area
# import math as m
# def radius(r):
#     return m.pi*(r**2)

    
# user_input = float(input("Please enter the radius of the circle: "))

# print(f"The area of the circle with radius {user_input} is {radius(user_input).__round__(4)}")

# Write a Python program to check if a number is positive, negative or zero

# def num_check(num):
#     if num == 0:
#         print("Number is 0")
#     elif num>0:
#         print("Number is greater than zero")
#     else:
#         print("Number is less than zero")

# num_check(2)
# num_check(0)
# num_check(-55)

'''Write a Python function to check whether a number is completely 
divisible by another number. Accept two integer values form the user'''

# def div(num1,num2):
#     if num1%num2 == 0:
#         print(f"{num1} is completely divisible by {num2}")
#     elif num2%num1 == 0:
#         print(f"{num2} is completely divisible by {num1}")
#     else:
#         print("They are not completely divisible by each other")

# div(10,10)
# div(12,6)
# div(5,10)


# Write a Python program that accepts an integer (n) and computes the value of (n + nn + nnn)

# user_input = int(input("Please enter any integer value: "))
# print(user_input+(user_input*user_input)+(user_input*user_input*user_input))

# Write a Python program to calculate number of days between two dates
#subtraction gives values in thousands, find way to bypass!!!!!!
# date1 = input("Enter the date in dd-mm-yy format: ")
# date1_int = int("".join([x for x in date1 if str.isnumeric(x)]))

# date2 = input("Enter the date in dd-mm-yy format: ")
# date2_int = int("".join([x for x in date2 if str.isnumeric(x)]))

# if date1_int >= date2_int:
#     print(f"The number of days between {date1} and {date2} are {date1_int - date2_int}")
# else:
#     print(f"The number of days between {date2} and {date1} are {date2_int - date1_int}")


'''Write a Python program to get the volume of a sphere, 
please take the radius as input from user. V=4 / 3 πr3'''

# import math as m
# def radius(r):
#     return (4/3)*(m.pi)*(r**3)

    
# user_input = float(input("Please enter the radius of the circle: "))

# print(f"The volume of the circle with radius {user_input} is {radius(user_input).__round__(4)}")

'''Write a Python program to get the 
difference between a given number and 17, difference cannot be negative'''

# user_input = int(input("Enter any number: "))

# if (user_input - 17) < 0:
#     print(f"The difference between {user_input} and 17 is {user_input-17} and it cannot be negative")
# else:
#     print(f"The difference is {user_input-17}")


'''Write a Python program to get a new string from a given string where "Is" has been added 
to the front. If the given string already begins with "Is" then return the string unchanged'''

# user_input = input("enter a string: ")
# if user_input[0] == "I" and user_input[1] == "s":
#     print(f"String: {user_input}")
# else:
#     user_input = "Is " + user_input
#     print(f"String: {user_input}")


'''Write a Python program to find whether a given number 
(accept from the user) is even or odd, print out an appropriate message to the user'''

# def even_odd(num):
#     if num%2 == 0:
#         return("even")
#     else:
#         return("odd")

# user_input = int(input("Please enter an integer: "))
# print(f"The entered number is {user_input} and it is {even_odd(user_input)}")


# Write a Python program to test whether a passed letter is a vowel or not

# user_input = input("Enter a letter: ")
# vowels = ['a','e','i','o','u']
# if user_input in vowels:
#     print("The entered letter is a vowel")
# else:
#     print("The entered letter is not a vowel")


'''Write a Python program that will return 
true if the two given integer values are equal or their sum or difference is 5.'''

# def true_or_not(num1,num2):
#     if num1 == num2 or (num1 + num2 == 5 or num1 - num2 == 5):
#         return True
#     else:
#         return ("no")

# user_input1 = int(input("Enter a number:"))
# user_input2 = int(input("Enter a number:"))

# print(true_or_not(user_input1,user_input2))


# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 

