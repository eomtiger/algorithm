king, queen, rook, bishop, knight, pone= map(int, input().split())

lst1 = [king, queen]
lst2 = [rook, bishop, knight]
lst3 = []
for i in range(2):

    if lst1[i] == 1:
        lst3.append(0)
    elif lst1[i] != 1:
        lst3.append(1 -lst1[i])

for i in range(3):

    if lst2[i] == 2:
        lst3.append(0)
    elif lst2[i] != 2:
        lst3.append(2-lst2[i])

if pone == 8:
    lst3.append(0)
elif pone !=8:
    lst3.append(8-pone)

for i in range(len(lst3)):
    print(lst3[i], end=' ')
