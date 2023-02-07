N = int(input())
number_list = []


def calc_decreasing_number(idx, number):
    if (number != ''):
        number_list.append(int(number))

    for i in range(0, idx):
        calc_decreasing_number(i, number + str(i))


calc_decreasing_number(10, '')

number_list.sort()

if (N >= len(number_list)):
    print(-1)
else:
    print(number_list[N])
