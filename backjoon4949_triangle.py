# from collections import deque
que = []
total = []
while True:
    inp = input().split('(')


    for i in inp:
        B = i.split(')')
        for i in B:
            total.append(i)
    print(total)
