N, K = map(int, input().split())
order_list = list(map(int, input().split()))
tab_list = []

cnt = 0

for i in range(len(order_list)):
    order = order_list[i]
    if (order in tab_list):
        continue
    elif (len(tab_list) < N):
        tab_list.append(order)
    else:
        cnt += 1
        remain_dis_list = []
        remain_order_list = order_list[i + 1::]
        for tab in tab_list:
            duplicate_dis = 0
            for remain_order in remain_order_list:
                if (remain_order != tab):
                    duplicate_dis += 1
                else:
                    break
            remain_dis_list.append(duplicate_dis)
        min_idx = remain_dis_list.index(max(remain_dis_list))
        del tab_list[min_idx]
        tab_list.append(order)

print(cnt)
