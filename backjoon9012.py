N = int(input())
for i in range(N):
    b = input()
    temp = False  
    arr = []  
    for j in b:
        if j == '(':
            arr.append(j)    
        else:
            if not arr:
                temp = True
                break
            arr.pop()
    if arr:
        temp = True

    if temp==True:
        print('NO')
    else:
        print('YES')
