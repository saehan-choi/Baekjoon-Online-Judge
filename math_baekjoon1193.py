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

# 골머리를 앓음



X=int(input())
line=1

# x는 입력된수
# line은 몇번 실행됬는지 알수있는수
# x가 line보다 무조건 작음
# 짝수번 실행되었으면 분모쪾에 line - X + 1

while X>line:
    X=X-line
    line+=1

if line%2==0:
    a=X
    b=line-X+1

else:
    a=line-X+1
    b=X

print(a, '/', b, sep='')
print(f'X : {X}')
print(f'line : {line}')
# X 는 배열안에 몇번째 index 인지 알수있음
# line은 몇번째 배열인지 알수있음

# [1/1], [1/2, 2/1], [3/1, 2/2, 1/3], [1/4, 2/3, 3/2, 4/1]
# 홀수번째 배열은 내림차순, 짝수번째 배열은 오름차순