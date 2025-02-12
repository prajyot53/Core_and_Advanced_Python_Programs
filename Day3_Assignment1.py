Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Take input from the user
... year = int(input("Enter a year: "))
Enter a year: 2005
>>> # Check for leap year using conditional statements
... if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
...     print(year, "is a leap year.")
... else:
...     print(year, "is not a leap year.")
... 
...     
2005 is not a leap year.
>>> #  Single line Comment :Python program to check leap year  or not.
... 
... #Input year from User
... year = int(input("Enter a year: "))
Enter a year: 2004
>>> # Leap year is divisible by 4 but not by 100, unless also divisible by 400
... if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
...     print("It is a leap year")
... else:
...      print("It is not a leap year")
... 
It is a leap year
>>> """ OUTPUT
... 
... Enter a year: 2004
... It is a leap year
