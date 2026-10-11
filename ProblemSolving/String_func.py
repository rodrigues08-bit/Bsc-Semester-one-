#To Reverse 
def reverse_string(text):
    return text[::-1]

# Get a string directly from the user
user_input = input("Enter a string to reverse: ")

# Call our custom function
reversed_input = reverse_string(user_input)

# Print the results without using f-strings
print("Original:", user_input)
print("Reversed:", reversed_input)

#To concatinate
def concat(str1, str2):
    return str1 + str2

# Get both strings from the user
first = input("Enter the first string: ")
second = input("Enter the second string: ")

# Call the function
result = concat(first, second)

# Print the result
print("Concatenated result:", result)