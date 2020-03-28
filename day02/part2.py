
def execute(code):
    pc = 0
    while True:
        if code[pc] == 1:
            code[code[pc + 3]] = code[code[pc + 1]] + code[code[pc + 2]]
            pc = pc + 4
        elif code[pc] == 2:
            code[code[pc + 3]] = code[code[pc + 1]] * code[code[pc + 2]]
            pc = pc + 4
        elif code[pc] == 99:
            break
        else:
            print("invalid opcode: " + str(code[pc]))
            exit(1)

def parse(input):
    return list(map(int, input.split(",")))

file = open("input.txt")
codes = parse(file.readline())

for noun in range(100):
    for verb in range(100):
        copy = codes.copy()
        copy[1] = noun
        copy[2] = verb
        execute(copy)

        if copy[0] == 19690720:
            print(100 * noun + verb)

