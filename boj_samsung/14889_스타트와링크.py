from collections import deque

def cal(li,temp): #temp = [0]
    if len(temp) == 3:
        temp = temp[1:]
        print(temp)
        return
    for i in range(len(temp), len(start)):
        temp.append(li[i])
        cal(li, temp)
        temp.pop()


def comb(arr, start):
   if len(start) == N//2+1:
       start=start[1:]
       link = []
       for i in arr:
           if i not in start:
               link.append(i)
    #    print(start)
    #    print(link)
    #    print('--------------------')
       
       cal(start, [0])
       cal(link,[0])
       return
       
   for i in range(start[-1], N): #start 중 제일 큰 수보다 1 더 큰 수부터 시작
       start.append(arr[i])
       comb(arr, start)
       start.pop()



N = int(input())

mat = [list(map(int, input().split())) for _ in range(N)]

arr = deque([])

for i in range(1, N+1):
    arr.append(i)

start = [0]

total = 9987654321

# print(len(start))

comb(arr, start)


