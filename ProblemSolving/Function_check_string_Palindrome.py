def check_palindrome(s):
    # Remove spaces and convert to lowercase for accurate checking
    formatted = s.replace(" ", "").lower()
    if formatted == formatted[::-1]:
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")

user_string = input("Enter a string: ")
check_palindrome(user_string)