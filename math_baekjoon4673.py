total_num = set(range(1,10001))  # 중복을 없에는 set함수 사용
add_num = set()

for i in range(len(total_num)):
    for j in str(i):
        i = i + int(j)
    add_num.add(i)

result = sorted(total_num - add_num)


for i in range(len(result)):
    print(result[i])

