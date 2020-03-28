
def calculate_fuel(mass):
    return max(0, mass // 3 - 2)

file = open("input.txt", "r")
lines = file.readlines()
sum = 0

for line in lines:
    mass = int(line)
    while mass > 0:
        fuel = calculate_fuel(mass)
        sum = sum + fuel
        mass = fuel

print(sum)