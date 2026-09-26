# Create a list of 5 names
names = ['Anil', 'Amol', 'Aditya', 'Avi', 'Alka']
print(names)

# Insert a name 'Anuj' before 'Aditya'
names.insert(2, 'Anuj')
print(names)

# Append a name 'Zulu'
names.append('Zulu')
print(names)

# Delete 'Avi' from the list
names.remove('Avi')
print(names)

# Replace 'Anil' with 'AnilKumar'
i = names.index('Anil')
names[i] = 'AnilKumar'
print(names)

# Sort all the names in the list
names.sort()
print(names)

# Print reversed sorted list
names.reverse()
print(names)