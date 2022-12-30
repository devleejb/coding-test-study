n = 1260
count = 0

coinList = [500, 100, 50, 10]

for coin in coinList:
    count += n // coin
    n %= coin

print(count)
