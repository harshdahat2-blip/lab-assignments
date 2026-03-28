# Task 1# ohms_law_current.py

v = float(input("Enter Voltage (V): "))
r = float(input("Enter Resistance (R): "))

current = v / r
print("Current =", current, "A")

if current < 0.5:
    print("Low current")
elif current <= 2:
    print("Normal current")
else:
    print("High current")

# Task 2# steel_grading.py

hardness = int(input("Enter hardness: "))
carbon = float(input("Enter carbon content: "))
tensile = int(input("Enter tensile strength: "))

c1 = hardness > 50
c2 = carbon < 0.7
c3 = tensile > 5600

if c1 and c2 and c3:
    grade = 10
elif c1 and c2:
    grade = 9
elif c2 and c3:
    grade = 8
elif c1 and c3:
    grade = 7
elif c1 or c2 or c3:
    grade = 6
else:
    grade = 5

print("Steel Grade:", grade)