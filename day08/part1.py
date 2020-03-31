
width = 25
height = 6

def parse_layers(input):
    size = width * height
    pixels = list(map(int, input))

    return [ pixels[i:i + size] for i in range(0, len(pixels), size) ]

def count_digit(pixels, digit):
    return sum(map(lambda p: p == digit, pixels))

file = open("input.txt", "r")
input = file.readline()

layers = parse_layers(input)
layer = min(layers, key=lambda layer: count_digit(layer, 0))
solution = count_digit(layer, 1) * count_digit(layer, 2)
print(solution)