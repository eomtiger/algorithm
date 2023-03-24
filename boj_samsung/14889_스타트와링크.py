

def cal(start, temp, s, val):
    global totalS, totalL
    # print(temp)
    if len(temp) == 2 and temp[0] != temp[1]:
        if val == 's':
            totalS += mat[temp[0]-1][temp[1]-1]
            totalS += mat[temp[1]-1][temp[0]-1]
        elif val == 'l':
            totalL += mat[temp[0]-1][temp[1]-1]
            totalL += mat[temp[1]-1][temp[0]-1]
        return

    for i in range(s, len(start)):
        temp.append(start[i])
        cal(start, temp, i+1, val)
        temp.pop()



def comb(arr, start, combV):

   global totalS, totalL, ans, visited
   # print(start)
   if combV == len(visited):
       return
   # print(start)
   if len(start) == N//2+1 and tuple(start[1:]) not in visited:
       start=start[1:]
       visited.add(tuple(start))
       # print(start)
       link = []
       for i in arr:
           if i not in start:
               link.append(i)
       visited.add(tuple(link))
       # print('link:', link)
       
       cal(start, [], 0, 's')
       # print('--------------')
       cal(link, [], 0, 'l')
       # print('///////////////////')
       # print(totalS)
       # print(totalL)
       # print('------------------------')

       ans = min(ans, abs(totalS-totalL))
       totalL = 0
       totalS = 0

       return
       
   for i in range(start[-1], N): #start 중 제일 큰 수보다 1 더 큰 수부터 시작
       if combV == len(visited):
           break
       start.append(arr[i])
       comb(arr, start, combV)
       start.pop()



N = int(input())

mat = [list(map(int, input().split())) for _ in range(N)]

arr = []

for i in range(1, N+1):
    arr.append(i)

start = [0]

ans = 9987654321
totalS = 0
totalL = 0

visited = set()

combV = 1
for i in range(N, N//2, -1):
    combV = combV * i

for i in range(1, N//2+1):
    combV = int(combV / i)

# print('com', combV)



comb(arr, start, combV)

print(ans)
