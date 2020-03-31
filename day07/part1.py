import itertools

def execute(code, inputs):
    pc = 0
    next_input = 0
    last_output = None

    def get_parameter(index):
        immediate_mode = code[pc] // 10**(index + 2) % 10 == 1

        if immediate_mode:
            return code[pc + index + 1]
        else:
            return code[code[pc + index + 1]]

    while True:
        opcode = code[pc] % 100

        if opcode == 1:
            code[code[pc + 3]] = get_parameter(0) + get_parameter(1)
            pc = pc + 4
        elif opcode == 2:
            code[code[pc + 3]] = get_parameter(0) * get_parameter(1)
            pc = pc + 4
        elif opcode == 3:
            code[code[pc + 1]] = inputs[next_input]
            next_input += 1
            pc += 2
        elif opcode == 4:
            last_output = get_parameter(0)
            print(last_output)
            pc += 2
        elif opcode == 5:
            if get_parameter(0) != 0:
                pc = get_parameter(1)
            else:
                pc += 3
        elif opcode == 6:
            if get_parameter(0) == 0:
                pc = get_parameter(1)
            else:
                pc += 3
        elif opcode == 7:
            code[code[pc + 3]] = 1 if get_parameter(0) < get_parameter(1) else 0
            pc += 4
        elif opcode == 8:
            code[code[pc + 3]] = 1 if get_parameter(0) == get_parameter(1) else 0
            pc += 4
        elif opcode == 99:
            return last_output
        else:
            print("invalid opcode: " + str(code[pc]))
            exit(1)

def parse(input):
    return list(map(int, input.split(",")))

file = open("input.txt")
codes = parse(file.readline())
# codes = parse("3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0")
# codes = parse("3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0")

best_output = 0
best_phases = []
for phases in itertools.permutations([0, 1, 2, 3, 4]):
    output = 0
    for phase in phases:
        output = execute(codes.copy(), [phase, output])
    
    if output > best_output:
        best_output = output
        best_phases = phases

print(best_output, best_phases)
