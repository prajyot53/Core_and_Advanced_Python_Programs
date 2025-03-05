Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # List of employee records with name and department details
>>> employees = [
...     {"name": "John Doe", "department": "Sales"},
...     {"name": "Jane Smith", "department": "Marketing"},
...     {"name": "Emily Johnson", "department": "Sales"},
...     {"name": "Michael Brown", "department": "HR"}
... ]
>>> 
>>> # Using list comprehension to filter employees from 'Sales' and convert names to uppercase
>>> sales_employees = [emp["name"].upper() for emp in employees if emp["department"] == "Sales"]
... 
>>> # Print the final list of sales employees' names in uppercase
>>> print(sales_employees)  # Output: ['JOHN DOE', 'EMILY JOHNSON']
['JOHN DOE', 'EMILY JOHNSON']
