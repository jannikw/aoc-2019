
class Node:
    def __init__(self, name):
        self.name = name
        self.orbits = []

    def add_orbiter(self, node):
        self.orbits.append(node)

    def count_orbits(self):
        return len(self.orbits) + sum(map(Node.count_orbits, self.orbits))

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

count = 0
for orbiter in orbit_map.values():
    count += orbiter.count_orbits()

print(count)