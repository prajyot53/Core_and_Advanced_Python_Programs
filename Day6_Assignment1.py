Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Take input from the user
... num = int(input("Enter a number: "))  # Example input: 1234
... 
... # Initialize variables
Enter a number: 1234
>>> reverse_num = 0  # Variable to store the reversed number
... 
... # Using while loop to reverse the number
>>> while num > 0:
...      digit = num % 10  # Get the last digit
...      reverse_num = (reverse_num * 10) + digit  # Append the digit to reverse_num
...      num = num // 10  # Remove the last digit from the original number
... 
>>> # Display the reversed number
>>> print("Reversed number:", reverse_num)  # Output: Reversed number: 4321
Reversed number: 4321
