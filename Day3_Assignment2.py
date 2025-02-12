Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Take input from the user
... a = int(input("Enter first number: "))
Enter first number: 2
>>> b = int(input("Enter second number: "))
Enter second number: 3
>>> c = int(input("Enter third number: "))
Enter third number: 4
>>> # Using conditional statements to find the largest number
... if a >= b and a >= c:
...     largest = a
... elif b >= a and b >= c:
...      largest = b
... else:
...     largest = c
...     # Display the largest number
...     print("The largest number is:", largest)
... 
...     
The largest number is: 4
