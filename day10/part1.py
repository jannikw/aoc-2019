import math

file = open("input.txt", "r")
lines = file.read().splitlines()

asteroids = [ (x, y) for y in range(0, len(lines))
                     for x in range(0, len(lines[y]))
                     if lines[y][x] == "#" ]

# Check if c is between a and b
def is_point_inbetween(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    len_ab = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    len_ac = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

    # Dot product of ab and ac
    dot_product = (x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1)

    # vectors must be parallel
    return math.isclose(dot_product, len_ab * len_ac) and len_ac < len_ab

best = None
best_count = 0

for pos in asteroids:
    others = list(filter(lambda p: p != pos, asteroids))
    count = 0
    for asteroid in others:
        collision = False
        for blocking in filter(lambda p: p != asteroid, others):
            if is_point_inbetween(pos, asteroid, blocking):
                collision = True
                break
        
        if not collision:
            count += 1

    if count > best_count:
        best_count = count
        best = pos

print(best)
print(best_count)