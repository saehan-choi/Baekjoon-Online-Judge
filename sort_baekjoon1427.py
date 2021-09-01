nums = input()

nums = [int(i) for i in nums]

nums.sort(reverse=True)

for i in nums:
    print(i,end="")

