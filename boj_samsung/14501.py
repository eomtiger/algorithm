def move(ac, acp):
    global total
    if ac == N:
        total = max(acp, total)
        return

    for i in range(ac+1, N+1):
        if i + arr[i][0]-1 <= N:
            move(i+arr[i][0]-1, acp+arr[i][1])
        elif  i + arr[i][0]-1 > N:
            total = max(acp, total)


N = int(input())

arr = {}
for i in range(N):
    b, c = map(int, input().split())

    arr[i+1] = (b, c)

ac = 0
acp = 0
total = 0

move(ac, acp)

print(total)




