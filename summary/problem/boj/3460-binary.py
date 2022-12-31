n_list = [bin(int(input())) for _ in range(int(input()))]

for n in n_list:
    bit_list = list(n)[2:]
    bit_list.reverse()
    result_list = []

    for i in range(len(bit_list)):
        if (bit_list[i] == '1'):
            result_list.append(i)

    print(*result_list)
