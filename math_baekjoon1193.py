# inp = int(input())

# i = 1
# floor = 0
# real_num = 0

# while True:    
#     floor = floor + i
#     if floor > inp:
#         real_num = floor - i 
#         break
#     i+=1
#     # print(floor)


# print(f'floor:{floor}')
# print(f'real_num:{real_num}')

# print(f'{floor-inp}/{floor-real_num}')
# print(f'real_num:{real_num}')
# # print(f'i:{i}')
# print(floor)

# real_num은 제일가까운 수를 찾아줌 거기서 몇번 더가면 됨.

# 골머리를 매우앓음




X=int(input())

line=1
while X>line:
    X-=line
    line+=1
print(X)
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')
