import sys
import math

input()

number_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

def calc_min(plus_cnt, minus_cnt, multiply_cnt, divide_cnt, idx, result):
    min = sys.maxsize
    if (idx == len(number_list)):
        return result

    if (plus_cnt):
        compare = calc_min(plus_cnt - 1, minus_cnt, multiply_cnt, divide_cnt, idx + 1, result + number_list[idx])
        min = compare if min > compare else min
    if (minus_cnt):
        compare = calc_min(plus_cnt, minus_cnt - 1, multiply_cnt, divide_cnt, idx + 1, result - number_list[idx])
        min = compare if min > compare else min
    if (multiply_cnt):
        compare = calc_min(plus_cnt, minus_cnt, multiply_cnt - 1, divide_cnt, idx + 1, result * number_list[idx])
        min = compare if min > compare else min
    if (divide_cnt):
        sign = 1 if result > 0 else -1
        compare = calc_min(plus_cnt, minus_cnt, multiply_cnt, divide_cnt - 1, idx + 1, sign * (abs(result) // number_list[idx]))
        min = compare if min > compare else min
    
    return min

def calc_max(plus_cnt, minus_cnt, multiply_cnt, divide_cnt, idx, result):
    max = -sys.maxsize + 1
    if (idx == len(number_list)):
        return result

    if (plus_cnt):
        compare = calc_max(plus_cnt - 1, minus_cnt, multiply_cnt, divide_cnt, idx + 1, result + number_list[idx])
        max = compare if max < compare else max
    if (minus_cnt):
        compare = calc_max(plus_cnt, minus_cnt - 1, multiply_cnt, divide_cnt, idx + 1, result - number_list[idx])
        max = compare if max < compare else max
    if (multiply_cnt):
        compare = calc_max(plus_cnt, minus_cnt, multiply_cnt - 1, divide_cnt, idx + 1, result * number_list[idx])
        max = compare if max < compare else max
    if (divide_cnt):
        sign = 1 if result > 0 else -1
        compare = calc_max(plus_cnt, minus_cnt, multiply_cnt, divide_cnt - 1, idx + 1,  sign * (abs(result) // number_list[idx]))
        max = compare if max < compare else max
    
    return max

print(calc_max(op_list[0], op_list[1], op_list[2], op_list[3], 1, number_list[0]))
print(calc_min(op_list[0], op_list[1], op_list[2], op_list[3], 1, number_list[0]))
