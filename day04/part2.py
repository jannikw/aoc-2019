
start = 168630
end = 718098

def contains_double_digit(number):
    if number in {000000, 111111, 222222, 333333, 444444, 555555, 666666, 777777, 888888, 999999}:
        return False

    lastFive = number % 100000
    if lastFive in {00000, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999}:
        return False
    
    
    while number >= 10:
        lastTwo = number % 100
        lastThree = number % 1000
        lastFour = number % 10000

        if number >= lastFour and lastFour in {0000, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999}:
            number //= 10000
        elif number >= lastThree and lastThree in {000, 111, 222, 333, 444, 555, 666, 777, 888, 999}:
            number //= 1000
        elif lastTwo in {00, 11, 22, 33, 44, 55, 66, 77, 88, 99}:
            return True
        else:
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

# print(check_password(112233))
# print(check_password(123444))
# print(check_password(111122))
# print(contains_double_digit(000000))
# print(contains_double_digit(999999))
# print(contains_double_digit(114444))
# print(contains_double_digit(334555))

count = 0
for number in range(start, end + 1):
    if check_password(number):
        count += 1

print(count)
