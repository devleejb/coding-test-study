S = int(input())
n = 0
k = S

while (2 * (n + 1) < S and S > 0):
    n += 1
    S -= n
    k = S

print(n + (1 if k > 0 else 0))
