
def execute(code):
    pc = 0

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
            code[code[pc + 1]] = int(input())
            pc += 2
        elif opcode == 4:
            print(get_parameter(0))
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
            break
        else:
            print("invalid opcode: " + str(code[pc]))
            exit(1)

def parse(input):
    return list(map(int, input.split(",")))

file = open("input.txt")
codes = parse(file.readline())

execute(codes)
