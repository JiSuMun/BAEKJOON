import sys
input = sys.stdin.readline
N = int(input())
while 1:
    flag = True
    for i in str(N):
        if i != '4'  and i != '7':
            flag = False
            N -= 1
    if flag:
        print(N)
        break