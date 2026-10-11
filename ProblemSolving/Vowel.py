# Get a string from the user
v = input("Enter a string: ")
vowels = "aeiouAEIOU"

# Set up a counter
vowel_c = 0

# Loop through each character in the string
for ch in v:
    # Check if the character is a vowel
    if ch in vowels:
        vowel_c += 1

# Print the final result
print("Number of vowels:", vowel_c)