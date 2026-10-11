# Create an empty dictionary
marks = {}

# Ask the user how many records they want to create
students = int(input("How many students do you want to add? "))

# Loop to get user input for each student
for i in range(students):
    name = input("Enter student name: ")
    # Using string concatenation (+) to avoid f-strings based on your previous preference
    m = float(input("Enter marks for " + name + ": "))

    # Add the key-value pair to the dictionary
    marks[name] = m

print("\nFinal Dictionary:", marks)

#update 
# Starting dictionary
s_marks = {'Aira': 85.0, 'Wayne': 92.0, 'Charlie': 78.5}
print("Current Dictionary:", s_marks)

# Get the key to update from the user
update = input("Enter the name of the student to update: ")

# Check if the key actually exists before trying to update it
if update in s_marks:
    n_marks = float(input("Enter the new marks: "))
    
    # Update the value for that specific key
    s_marks[update] = n_marks
    
    print("Updated Dictionary:", s_marks)
else:
    print("Error:",update, "is not in the dictionary.")

#printing report 
# Create an empty dictionary and populate it with user input
data = {}
entries = int(input("How many entries do you want to add? "))

for i in range(entries):
    k = input("Enter student name (Key): ")
    v= input("Enter marks (Value): ")
    data[k] = v

print("\n--- Dictionary Contents ---")

# .items() grabs both the key and the value for each loop iteration
for k, v in data.items():
    print("Student:", k, "| Marks:", v)