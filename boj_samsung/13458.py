N = int(input())

arr = list(map(int, input().split()))

b, c = map(int, input().split())

total = N
for i in range(N):
    arr[i] = arr[i] - b

    if arr[i] <=0:
        pass

    else:
        q = arr[i] // c
        r = arr[i] % c
        if r != 0:
            total += q + 1
        elif r == 0 and q:
            total += q


print(total)
