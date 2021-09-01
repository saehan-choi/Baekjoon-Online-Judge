N = int(input())

count = 99

if N < 100:
    print(N)

else:
    for i in range(100,N+1):
        arr2 = []
        for j in str(i):
            arr2.append(int(j))
            
        if arr2[1]-arr2[0] == arr2[2]-arr2[1]:
            count+= 1

    print(count)
            

# memory: 29200kb	
# time:68ms