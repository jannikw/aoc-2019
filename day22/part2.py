size = 119315717514047
repeat = 101741582076661

# f(x) = -x - 1 mod size
def deal_into_new_stack():
    return (-1, -1)

# f(x) = x - n mod size
def cut(n):
    return (1, -n)

# f(x) = x * n mod size
def deal_with_increment(n):
    return (n, 0)

# f(x) = a * x + b mod size
# g(x) = c * x + d mod size
# f(g(x)) = a * (c * x + d) + b mod size
#         = a * c * x + a * d + b mod size
def compose(f, g):
    return (f[0] * g[0] % size, (f[0] * g[1] + f[1]) % size)

# Repeated composition to get f^n(x)
def repeat_steps(f, n):
    r = (1, 0)

    while n > 0:
        if n % 2 == 1:
            r = compose(r, f)
            n = n - 1
        else:
            f = compose(f, f)
            n = n // 2

    return r

# Calculare f(x)
def evaluate(f, x):
    return (f[0] * x + f[1]) % size

# Modular multiplicative inverse for a to modulus m
def mod_inverse(a, m):
    return ext_euclid(m, a)[2] % m

def ext_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    
    x = ext_euclid(b, a % b)
    return (x[0], x[2], x[1] - (a // b) * x[2])


def do_compose_steps():
    file = open("input.txt", "r")
    lines = file.readlines()
    f = (1, 0)

    for line in lines:
        if line.startswith("deal into new stack"):
            f = compose(deal_into_new_stack(), f)
        elif line.startswith("cut"):
            n = int(line.split()[-1])
            f = compose(cut(n), f)
        elif line.startswith("deal with increment"):
            n = int(line.split()[-1])
            f = compose(deal_with_increment(n), f)
        else:
            print("error: " + line)
            exit(1)

    return f

composed_steps = do_compose_steps()
repeated_steps = repeat_steps(composed_steps, repeat)

# Determine card on position 2020: y = f(x) = 2020
y = 2020
x = (y - repeated_steps[1]) * mod_inverse(repeated_steps[0], size) % size

# Print actual result
print(x)

# Test: Should print 2020
print(evaluate(repeated_steps, x))