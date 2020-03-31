
width = 25
height = 6

def parse_layers(input):
    size = width * height
    pixels = list(map(int, input))

    return [ [ pixels[h:h + width] for h in range(i, i + size, width) ] for i in range(0, len(pixels), size) ]

def get_pixel(layers, x, y):
    for layer in layers:
        pixel = layer[y][x]

        if pixel == 0 or pixel == 1:
            return pixel

    return 2

file = open("input.txt", "r")
input = file.readline()

layers = parse_layers(input)
image = [ [ get_pixel(layers, x, y) for x in range(0, width) ] for y in range(0, height) ]

for line in image:
    for pixel in line:
        print("X" if pixel == 1 else " ", end="")
    print()