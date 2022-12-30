numberList = map(int, list(input()))
maxSum = 0

for number in numberList:
    if (maxSum * number > maxSum + number):
        maxSum *= number
    else:
        maxSum += number

print(maxSum)
