
class Node:
    def __init__(self, name):
        self.name = name
        self.orbits = []

    def add_orbiter(self, node):
        self.orbits.append(node)

    def count_orbits(self):
        return len(self.orbits) + sum(map(Node.count_orbits, self.orbits))

    def get_orbits(self):
        return self.orbits

    def get_name(self):
        return self.name

file = open("input.txt", "r")
lines = file.read().splitlines()

com = Node("COM")
orbit_map = {
    "COM": com
}

def get_orbiter(name):
    if name in orbit_map.keys():
        return orbit_map[name]
    else:
        orbiter = Node(name)
        orbit_map[name] = orbiter
        return orbiter

for line in lines:
    orbitee_name, orbiter_name = line.split(")")

    orbiter = get_orbiter(orbiter_name)
    orbitee = get_orbiter(orbitee_name)
    orbitee.add_orbiter(orbiter)
    orbit_map[orbiter_name] = orbiter

def get_neighbours(orbiter_name):
    orbiter = orbit_map[orbiter_name]
    parent = None
    for o in orbit_map.values():
        if orbiter in o.get_orbits():
            parent = o
            break

    return ([parent] if parent != None else []) + orbiter.get_orbits()

# Dijkstra Search
def find_path(start, finish):
    distances = {}
    unvisited = set()
    for name in orbit_map.keys():
        distances[name] = None
        unvisited.add(name)
    distances[start] = 0

    while len(unvisited) > 0:
        current = min(filter(lambda name: distances[name] != None, unvisited), key=lambda name: distances[name])
        neighbours = get_neighbours(current)

        for neighbour in neighbours:
            name = neighbour.get_name()

            if distances[name] == None or distances[name] > distances[current] + 1:
                distances[name] = distances[current] + 1

        unvisited.remove(current)

    return distances[finish]

# Subtract 2 since the first and the last step don't count
distance = find_path("YOU", "SAN") - 2
print(distance)
    