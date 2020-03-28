
def calculate_fuel(mass):
    return mass // 3 - 2

file = open("input.txt", "r")
lines = file.readlines()
sum = 0

for line in lines:
    mass = int(line)
    fuel = calculate_fuel(mass)
    sum = sum + fuel

print(sum)
