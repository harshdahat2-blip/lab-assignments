Task 1
print("PATTERN 1")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nPATTERN 2")
for i in range(1, 6):
    print(str(i) * i)

print("\nPATTERN 3")
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

print("\nPATTERN 4")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j % 2, end="")
    print()

print("\nPATTERN 5")
num = 2
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()

print("\nPATTERN 6")
for i in range(1, 6):
    print("*" * i)

print("\nPATTERN 7")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print("\nPATTERN 8")
for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print("#", end="")
        else:
            print("*", end="")
    print()

print("\nPATTERN 9")
chars = ['p', 'y', 't', 'h', 'o']
for i in range(len(chars)):
    print(chars[i] * (i + 1))

print("\nPATTERN 10")
word = "python"
for i in range(1, len(word) + 1):
    print(word[:i])

#Task 2
print("PATTERN 1")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print("\nPATTERN 2")
for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print("#", end="")
        else:
            print("*", end="")
    print()

print("\nPATTERN 3")
letters = "python"
for i in range(len(letters)):
    print(letters[i] * (i + 1))

print("\nPATTERN 4")
word = "python"
for i in range(1, len(word) + 1):
    print(word[:i])


#Task 3
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i, end="")

#Task 4
rows = 5

for i in range(rows):
    print(" " * i, end="")
    for j in range(rows - i):
        print("*", end=" ")
    print()

#Task 5
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()
    

#Task 7
while True:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    if start < end:
        break
    print("Start must be less than end. Try again.")

print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
