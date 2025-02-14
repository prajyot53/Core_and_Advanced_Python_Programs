Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Take input from the user
... num = int(input("Enter a number: "))  # Example input: 5
... 
Enter a number: 5
>>> # Initialize factorial result
>>> factorial = 1  
... 
>>> # Initialize counter variable
>>> i = num
>>> # Using while loop to calculate factorial
>>> while i > 0:
...     factorial *= i  # Multiply factorial by current value of i
...     i -= 1  # Decrease i by 1
... 
...     
>>> # Display the factorial result
>>> print("Factorial of", num, "is:", factorial)  # Output: Factorial of 5 is: 120
Factorial of 5 is: 120
