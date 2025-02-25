Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_integer():
...     """
...     Prompts the user to enter an integer.
...     Raises a ValueError if the input is not a valid integer.
...     """
...     try:
...         # Taking input from user
...         user_input = input("Enter an integer: ")
... 
...         # Attempt to convert the input to an integer
...         number = int(user_input)
... 
...         # Return the valid integer
...         return number
...     except ValueError:
...         # Raise a ValueError if conversion fails
...         raise ValueError("Invalid input! Please enter a valid integer.")
... 
...     
>>> # Example usage
>>> if __name__ == "__main__":
...     try:
...         integer_value = get_integer()
...         print(f"You entered the integer: {integer_value}")
...     except ValueError as e:
...         print(e)
... 
...         
Enter an integer: 5
You entered the integer: 5
