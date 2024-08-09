#Problem 1: Reverse a String

def reverse_string(s):
    return s[::-1]

# Taking input from the user
user_input = input("Enter a string to reverse: ")
print("Reversed string:", reverse_string(user_input))