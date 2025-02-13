Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Function definition: div() takes two parameters and returns their division
... def div(a, b):
...      if b == 0:
...          return "Error! Division by zero is not allowed."
...      return a / b
...     # Taking input from the user
... 
...     
>>> num1 = float(input("Enter the first number: "))
Enter the first number: 10
>>> num2 = float(input("Enter the second number: "))
Enter the second number: 2
>>> # Function call and result display
>>> result = div(num1, num2)
>>> print("Division result:", result)  # Output: Division result: 5.0
Division result: 5.0
