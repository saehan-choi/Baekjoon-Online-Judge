
inp = int(input())
arr = []
for i in range(inp):
    k = int(input())
    if k == 0:
        if arr:
            arr.sort()
            print(arr.pop())    
        else:
            print(0)
    else:
        arr.append(k)

# print(arr)
# inp = int(input())
# arr = [1,2,3,6,7,2,4,2,3,4]
# arr.sort()
# print(arr.pop())

