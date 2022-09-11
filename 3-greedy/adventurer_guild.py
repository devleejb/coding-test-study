n = int(input())
scareList = list(map(int, input().split()))
member = 0  # 현재 그룹의 모험가 수
groupCount = 0  # 그룹 카운트

scareList.sort()

for scare in scareList:
    member += 1

    if (scare <= member):
        groupCount += 1
        member = 0

print(groupCount)
