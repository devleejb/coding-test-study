a, b = map(int, input().split())


def gcd(a, b):
    while (a % b):
        a, b = b, a % b
    return b


def lcm(a, b):
    return a * b / gcd(a, b)


print(gcd(a, b))
print(int(lcm(a, b)))
