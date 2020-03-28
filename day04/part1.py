
start = 168630
end = 718098

def contains_double_digit(number):
    while number >= 10:
        lastTwoDigits = number % 100

        if lastTwoDigits in {00, 11, 22, 33, 44, 55, 66, 77, 88, 99}:
            return True

        number //=  10

    return False

def digit(num, d):
    return num // 10**d % 10

def never_decreases(number):
    last = 0
    for i in range(5, -1, -1):
        x = digit(number, i)

        if x < last:
            return False

        last = x

    return True

def check_password(number):
    return contains_double_digit(number) and never_decreases(number)

# print(check_password(111111))
# print(check_password(223450))
# print(check_password(123789))
# print(never_decreases(135679))
# print(never_decreases(111123))
# print(contains_double_digit(122345))
# print(contains_double_digit(123456))

count = 0
for number in range(start, end + 1):
    if check_password(number):
        count += 1

print(count)
