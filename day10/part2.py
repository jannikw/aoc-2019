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

def get_angle_and_distance(a, b):
    x1, y1 = a
    x2, y2 = b

    len_ab = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    angle = math.acos((y1 - y2) / len_ab) if x2 >= x1 else 2 * math.pi - math.acos((y1 - y2) / len_ab)

    return (angle, len_ab)

station = (26, 29)
asteroids.remove(station)

non_blocked = []
for asteroid in asteroids:
    blocked = False
    for other in asteroids:
        if is_point_inbetween(station, asteroid, other):
            blocked = True
            break

    if not blocked:
        non_blocked.append(asteroid)

angles_and_distances = list(map(lambda asteroid: (asteroid, *get_angle_and_distance(station, asteroid)), non_blocked))
rotation_angle = -0.0000001

for i in range(0, 200):
    next = sorted(filter(lambda x: x[1] > rotation_angle, angles_and_distances), key=lambda x: (x[1], x[2]))[0]
    angles_and_distances.remove(next)
    rotation_angle = next[1]

    print(i + 1, next[0])



