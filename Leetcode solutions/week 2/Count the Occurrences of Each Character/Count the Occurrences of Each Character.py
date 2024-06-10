def count_char_occurrences(s):
    from collections import Counter
    return Counter(s)

# Taking input from the user
user_input = input("Enter a string to count character occurrences: ")
char_count = count_char_occurrences(user_input)
print("Character occurrences:", char_count)