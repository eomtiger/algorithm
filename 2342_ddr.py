import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

arr = list(map(int, input().split()))
a = {}
n = len(arr) - 1

for i in range(5):
    for j in range(5):
        a[(i, j)] = {}



res = 987654321

def move(l, r, score, turn):
    global res

    if score > res:
        return

    if len(arr)-2 == turn:          #끝까지 가면 리턴
        if score < res:
            res = score
        return

    #왼발을 움직일 때

    if l != 0 and abs(l-arr[turn+1]) == 1: #발을 옮기는데 차이가 1일 때
        if r == arr[turn+1]:    #오른발이 이미 있을 때
            pass
        else:
            v = a[(arr[turn + 1], r)].get(turn + 1)

            if v == None:
                a[(arr[turn + 1], r)][turn + 1] = score + 3
                move(arr[turn + 1], r, score + 3, turn + 1)

            elif a[(arr[turn+1], r)][turn+1] > score+3:
                a[(arr[turn+1], r)][turn+1] = score+3
                move(arr[turn+1], r, score+3, turn+1)

    elif l != 0 and abs(l-arr[turn+1]) == 2: #발을 옮기는데 차이가 2일 때
        if r == arr[turn+1]:    #오른발이 이미 있을 때
            pass
        else:
            v = a[(arr[turn + 1], r)].get(turn + 1)
            if v == None:
                a[(arr[turn + 1], r)][turn + 1] = score + 4
                move(arr[turn + 1], r, score + 4, turn + 1)

            elif a[(arr[turn+1], r)][turn+1] > score+4:
                a[(arr[turn+1], r)][turn+1] = score+4
                move(arr[turn+1], r, score+4, turn+1)

    elif l == arr[turn+1]:      #같은 위치라면
        v = a[(arr[turn + 1], r)].get(turn + 1)

        if v == None:
            a[(arr[turn + 1], r)][turn + 1] = score + 1
            move(arr[turn + 1], r, score + 1, turn + 1)

        elif a[(arr[turn + 1], r)][turn + 1] > score + 1:
            a[(arr[turn + 1], r)][turn + 1] = score + 1
            move(arr[turn + 1], r, score + 1, turn + 1)

    elif l == 0:          #발이 가운데 있을 때
        if r == arr[turn+1]:    #오른발이 이미 있을 때
            pass
        else:
            v = a[(arr[turn+1], r)].get(turn+1)
            if v == None:
                a[(arr[turn + 1], r)][turn + 1] = score + 2
                move(arr[turn + 1], r, score + 2, turn + 1)

            elif a[(arr[turn+1], r)][turn+1] > score+2:
                a[(arr[turn+1], r)][turn+1] = score+2
                move(arr[turn+1], r, score+2, turn+1)


    #오른발을 움직일 때

    if r != 0 and abs(r-arr[turn+1]) == 1: #발을 옮기는데 차이가 1일 때
        if l == arr[turn+1]:    #왼발이 이미 있을 때
            pass
        else:
            v = a[(l, arr[turn + 1])].get(turn + 1)
            if v == None:
                a[(l, arr[turn + 1])][turn + 1] = score + 3
                move(l, arr[turn + 1], score + 3, turn + 1)

            elif a[(l, arr[turn+1])][turn+1] > score+3:
                a[(l, arr[turn+1])][turn+1] = score+3
                move(l, arr[turn+1], score+3, turn+1)

    elif r != 0 and abs(r-arr[turn+1]) == 2: #발을 옮기는데 차이가 2일 때
        if l == arr[turn+1]:    #왼발이 이미 있을 때
            pass
        else:
            v = a[(l, arr[turn + 1])].get(turn + 1)
            if v == None:
                a[(l, arr[turn + 1])][turn + 1] = score + 4
                move(l, arr[turn + 1], score + 4, turn + 1)

            elif a[(l, arr[turn+1])][turn+1] > score+4:
                a[(l, arr[turn+1])][turn+1] = score+4
                move(l, arr[turn+1], score+4, turn+1)

    elif r == arr[turn+1]:      #같은 위치라면
        v = a[(l, arr[turn + 1])].get(turn + 1)
        if v == None:
            a[(l, arr[turn + 1])][turn + 1] = score + 1
            move(l, arr[turn + 1], score + 1, turn + 1)

        elif a[(l, arr[turn + 1])][turn + 1] > score + 1:
            a[(l, arr[turn + 1])][turn + 1] = score + 1
            move(l, arr[turn + 1], score + 1, turn + 1)

    elif r == 0:          #발이 가운데 있을 때
        if l == arr[turn+1]:    #왼발이 이미 있을 때
            pass
        else:
            v = a[(l, arr[turn + 1])].get(turn + 1)
            if v == None:
                a[(l, arr[turn + 1])][turn + 1] = score + 2
                move(l, arr[turn + 1], score + 2, turn + 1)

            elif a[(l, arr[turn+1])][turn+1] > score+2:
                a[(l, arr[turn+1])][turn+1] = score+2
                move(l, arr[turn+1], score+2, turn+1)


move(0, 0, 0, -1)
# print(a)
print(res)



