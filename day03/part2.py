
def parse_wire_directions(line):
    return [ (part[0], int(part[1:])) for part in line.split(",") ]

def wire_segments(directions):
    x = 0
    y = 0
    segments = []
    steps = 0

    for direction in directions:
        start = (x, y)

        if direction[0] == "U":
            y = y + direction[1]
        elif direction[0] == "R":
            x = x + direction[1]
        elif direction[0] == "D":
            y = y - direction[1]
        elif direction[0] == "L":
            x = x - direction[1]
            
        steps += direction[1]
        end = (x, y)
        segments.append((start, end, steps))

    return segments

# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
def line_intersection(line1, line2):
    (x1, y1), (x2, y2), _ = line1
    (x3, y3), (x4, y4), _ = line2

    div = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

    if div == 0:
        return None

    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) // div
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y4 * x4)) // div

    return (x, y)

def is_point_on_line(point, line):
    x, y = point
    (x1, y1), (x2, y2), _ = line

    if x1 == x2:
        return y > min(y1, y2) and y < max(y1, y2)
    else:
        return x > min(x1, x2) and x < max(x1, x2)

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

file = open("input.txt", "r")
lines = file.readlines()
line1 = lines[0]
line2 = lines[1]
# line1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
# line2 = "U62,R66,U55,R34,D71,R55,D58,R83"
# line1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
# line2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

wire1 = wire_segments(parse_wire_directions(line1))
wire2 = wire_segments(parse_wire_directions(line2))
intersections = []

for line1 in wire1:
    for line2 in wire2:
        intersection = line_intersection(line1, line2)

        if intersection != None and is_point_on_line(intersection, line1) and is_point_on_line(intersection, line2):
            distance1 = manhattan_distance(line1[1], intersection)
            distance2 = manhattan_distance(line2[1], intersection)
            steps = line1[2] - distance1 + line2[2] - distance2
            intersections.append(steps)

steps = min(intersections)
print(steps)