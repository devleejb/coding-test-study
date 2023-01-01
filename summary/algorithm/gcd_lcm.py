a = 1112
b = 695


def gcd(a, b):
    while (a % b):
        a, b = b, a % b

    return b


def gcd2(a, b):
    return a if b == 0 else gcd2(b, a % b)


def lcm(a, b):
    return a * b / gcd2(a, b)


print(gcd(a, b))
print(lcm(a, b))
