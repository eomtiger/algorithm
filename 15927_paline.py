def paline(S):
    global maxL
    # print(list(reversed(S)))
    if S != list(reversed(S)) and len(S)> maxL:    #palindrome이 아니고 최대 길이보다 길다면
        maxL = len(S)
        return

    if len(S) != 0:                             #S의 길이가 0이 아니면
        S.pop()                                 #뒤부터 하나씩 빼고
        paline(S)                               #재귀


S = input()

maxL = 0

S = list(S)                 #문자열을 리스트로 바꾸고


if len(set(S)) == 1:        #set으로 바꿨을 때 문자가 하나면
    print(-1)               # -1

else:

    paline(S)                   #기본으로 한번 함수 돌리고 maxL 갱신

    while len(S) != 0:
        S.pop(0)                #S에서 맨 앞 문자열을 빼고
        if len(S) <= maxL:      #S 길이가 maxL보다 짧거나 같다면
            break               #break!

        paline(S)               #아니면 재귀함수로

    if maxL == 0:
        print(-1)
    else:
        print(maxL)




