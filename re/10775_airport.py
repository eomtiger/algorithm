import sys
input = sys.stdin.readline

G = int(input())  #게이트 수
P = int(input())  #비행기 수

docked = set()
cnt = 0
for _ in range(P):

    g = int(input())

    # if 1 in docked and g in docked:
    #     break

    flag = False
    for i in range(g, 0, -1):
        if i not in docked:
            docked.add(i)
            cnt += 1
            flag = True
            break
    if flag == False:
        break

# print(docked)
print(cnt)








