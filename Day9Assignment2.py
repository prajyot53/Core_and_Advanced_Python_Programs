#Python program to remove duplicate characters of a given string. 
def remove_duplicate_words(s):
    words = s.split()  # Split the string into a list of words
    seen = set()       # Set to store unique words
    result = []        # List to store result words

    # Iterate through each word in the list
    for word in words:
        if word not in seen:  # Check if the word is already encountered
            seen.add(word)    # Add new word to the set
            result.append(word)  # Append to result list

    return " ".join(result)  # Convert list back to string

# Given input string
input_str = "String and String Function"

# Call the function and store the result
output_str = remove_duplicate_words(input_str)

# Print the result
print("Output:", output_str)

# Output: String and Function


