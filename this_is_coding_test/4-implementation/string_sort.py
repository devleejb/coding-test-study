from curses.ascii import isdigit

S = input()
resultStr = ""
sum = 0

for character in S:
    if (isdigit(character)):
        sum += int(character)
    else:
        resultStr += character

print("".join(sorted(resultStr)) + str(sum))
