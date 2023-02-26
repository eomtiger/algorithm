import copy

N = int(input())

arr = list(map(int, input().split()))
res = 0
for a in range(N//2):
    res += arr[a*2]


for i in range(N//2):
    new_arr = copy.deepcopy(arr)
    bot = new_arr.pop()
    new_arr.insert(i*2, bot)

    sum_arr = 0
    for a in range(N//2):
        # print(sum_arr)
        sum_arr += new_arr[a*2]

    res = max(res, sum_arr)

print(res)