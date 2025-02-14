Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Take input from the user
... num = input("Enter a number: ")  # Example input: 121
Enter a number: 121
>>> # Reverse the number using a for loop
>>> reverse_num = ""
>>> for digit in num:
...     reverse_num = digit + reverse_num  # Append digits in reverse order
... 
...     
>>> # Check if the original number and reversed number are the same
>>> if num == reverse_num:
...     print(num, "is a palindrome.")
... else:
...     print(num, "is not a palindrome.")
... 
...     
121 is a palindrome.
