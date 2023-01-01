from itertools import combinations

high_list = combinations([int(input()) for _ in range(9)], 7)

for high in high_list:
    sum = 0

    for tall in list(high):
        sum += tall

    if (sum == 100):
        sorted_list = list(high)
        sorted_list.sort()

        for tall in sorted_list:
            print(tall)
