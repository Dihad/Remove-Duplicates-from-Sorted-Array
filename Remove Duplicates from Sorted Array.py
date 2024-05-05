nums = [0,0,1,1,1,2,2,3,3,4]
new_nums = []
count = 0
for num in nums:
    if num not in new_nums:
        new_nums.append(num)
    if num in new_nums:
        count=count+1
for i in range(count):
    new_nums.append('_')
print(new_nums)
