Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # List of email addresses
>>> emails = ["alice@example.com", "bob@sample.org", "charlie@mydomain.net"]
>>> 
>>> # Using list comprehension to extract the domain part (everything after '@')
>>> domains = [email.split("@")[1] for email in emails]
>>> 
>>> # Print the extracted domain names
>>> print(domains)  # Output: ['example.com', 'sample.org', 'mydomain.net']
['example.com', 'sample.org', 'mydomain.net']
