from collections import deque
def comb(arr, start, link):
    global total
    # print(total)
    if len(start) == N//2:
        link.extend(arr)
        arr.clear()
        print(start, link)

        total = min(total, abs(sum(start)-sum(link)))
        return

    elif len(link) == N//2:
        start.extend(arr)
        arr.clear()
        total = min(total, abs(sum(start)-sum(link)))
        return

    if arr:
        temp = arr.popleft()
    else: return
    start.append(temp)
    comb(arr, start, link)
    start.pop()
    link.append(temp)
    comb(arr, start, link)



N = int(input())

mat = [list(map(int, input().split())) for _ in range(N)]

arr = deque([])

for i in range(1, N+1):
    arr.append(i)

start = []
link = []
total = 9987654321

# print(len(start))

comb(arr, start, link)

print(total)

