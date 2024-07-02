#Find All Substrings of a String
def find_substrings(s):
    substrings = []
    length = len(s)
    for i in range(length):
        for j in range(i+1, length+1):
            substrings.append(s[i:j])
    return substrings

# Taking input from the user
user_input = input("Enter a string to find all substrings: ")
print("All substrings:", find_substrings(user_input))