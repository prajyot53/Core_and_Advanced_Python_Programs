Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Python program to count letters, digits, and special symbols in a given string
>>> # Input string
>>> input_str = "P@#yn26at^&i5ve"
>>> # Initialize counters
>>> chars = digits = symbols = 0
>>> # Iterate through each character in the string
>>> for char in input_str:
...     if char.isalpha():  # Check if the character is a letter
...         chars += 1
...     elif char.isdigit():  # Check if the character is a digit
...         digits += 1
...     else:  # If not a letter or digit, it is a special symbol
...         symbols += 1
... 
>>> # Print the results
>>> print("Input:", input_str)
Input: P@#yn26at^&i5ve
>>> print(f"Output: Chars = {chars} Digits = {digits} Symbols = {symbols}")
Output: Chars = 8 Digits = 3 Symbols = 4
