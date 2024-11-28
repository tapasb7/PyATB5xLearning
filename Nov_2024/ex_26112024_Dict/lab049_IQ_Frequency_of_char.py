# Frequency of characters in a String.
# str = "automation"


str = input("Enter the input string : ")

char_count = {}
for char in str:
    char_count[char] = char_count.get(char, 0) +1

print(char_count)