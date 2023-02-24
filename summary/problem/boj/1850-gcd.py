A, B = map(int, input().split())


def gcd(a, b):
    if (a < b):
        a, b = b, a

    while (a % b):
        a, b = b, a % b
    return b


num_of_one = gcd(A, B)

while (num_of_one):
    print(1, end='')
    num_of_one -= 1
