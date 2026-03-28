#Task 1
s = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
lowercase = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    if ch == " ":
        spaces += 1
    if ch.islower():
        lowercase += 1

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Spaces:", spaces)
print("Number of Lowercase Letters:", lowercase)

#Task 2
def capitalize_lines():
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    for line in lines:
        print(line.upper())

capitalize_lines()