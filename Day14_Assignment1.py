Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Python program to handle ZeroDivisionError exception
... 
>>> def divide_numbers(a, b):
...      """
...     Function to divide two numbers with exception handling for ZeroDivisionError.
...     :param a: numerator (int or float)
...     :param b: denominator (int or float)
...     :return: division result or error message
...     """
...      try:
...          result = a / b
...          return result
...      except ZeroDivisionError:
...          return "Error: Division by zero is not allowed!"
... 
...         
>>> # Taking user input
>>> numerator = float(input("Enter the numerator: "))
Enter the numerator: 2.6
>>> denominator = float(input("Enter the denominator: "))
... 
Enter the denominator: 5.2
>>> # Calling the function and displaying the result
>>> print("Result:", divide_numbers(numerator, denominator))
Result: 0.5
