# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 
# 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 
# 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 
# 최소로 만드는 프로그램을 작성하시오.

A = input().split('-')

num = []
for i in A:
    cnt = 0
    B = i.split('+')
    for j in B:
        cnt+=int(j)
    num.append(cnt)

for i in range(1,len(num)):
    num[0]-=num[i]
print(num[0])