#input_string = "hello, world!"
#aeiou

str = input("Enter the string : ")

vowels = "aeiou"
vowels_count = 0

for i in str:
    if i in vowels:
        vowels_count += 1

print("no of vowels : ", vowels_count)