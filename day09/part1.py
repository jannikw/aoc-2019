import itertools

def execute(code):
    memory = {}
    for i in range(len(code)):
        memory[i] = code[i]

    pc = 0
    relative_base = 0

    def get_cell(address):
        return memory.setdefault(address, 0)

    def set_cell(address, value):
        memory[address] = value

    def get_parameter(index):
        mode = get_cell(pc) // 10**(index + 2) % 10

        if mode == 1: # immediate mode
            return get_cell(pc + index + 1)
        elif mode == 2: # relative mode
            return get_cell(relative_base + get_cell(pc + index + 1))
        else:
            return get_cell(get_cell(pc + index + 1))

    def get_address(index):
        mode = get_cell(pc) // 10**(index + 2) % 10

        if mode == 2: # relative mode
            return relative_base + get_cell(pc + index + 1)
        else:
            return get_cell(pc + index + 1)

    while True:
        opcode = get_cell(pc) % 100

        if opcode == 1:
            set_cell(get_address(2), get_parameter(0) + get_parameter(1))
            pc += 4
        elif opcode == 2:
            set_cell(get_address(2), get_parameter(0) * get_parameter(1))
            pc += 4
        elif opcode == 3:
            set_cell(get_address(0), int(input()))
            pc += 2
        elif opcode == 4:
            output = get_parameter(0)
            print(output)
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
            set_cell(get_address(2), 1 if get_parameter(0) < get_parameter(1) else 0)
            pc += 4
        elif opcode == 8:
            set_cell(get_address(2), 1 if get_parameter(0) == get_parameter(1) else 0)
            pc += 4
        elif opcode == 9:
            relative_base += get_parameter(0)
            pc += 2
        elif opcode == 99:
            return
        else:
            print("invalid opcode: " + str(get_cell(pc)))
            exit(1)

def parse(input):
    return list(map(int, input.split(",")))

file = open("input.txt")
codes = parse(file.readline())

execute(codes)
