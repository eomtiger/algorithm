import sys
input = sys.stdin.readline

pc = 0
gasanki = 0
memory_address = {}
x = 0
for _ in range(32):
    memory = input().rstrip()

    pc += 1

    if memory[0:3] == '000':
        x = gasanki

    elif memory[0:3] == '001':
        num = '0b' + memory[3::]
        gasanki = int(num, 2)

    elif memory[0:3] == '010':
        if gasanki == 0:
            num = '0b' + memory[3::]
            pc = int(num, 2)

    elif memory[0:3] == '011':
        pass

    elif memory[0:3] == '100':
        gasanki -= 1

    elif memory[0:3] == '101':
        gasanki += 1

    elif memory[0:3] == '110':
        num = '0b' + memory[3::]
        pc = int(num, 2)

    elif memory[0:3] == '111':
        break

print(gasanki)
ans = bin(gasanki)
print(ans)
print(ans[::-1])
