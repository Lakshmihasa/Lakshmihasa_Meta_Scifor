#Problem 3: Count Vowels in a String
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Taking input from the user
user_input = input("Enter a string to count vowels: ")
print("Number of vowels:", count_vowels(user_input))