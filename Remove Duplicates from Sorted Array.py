nums = [0,0,1,1,1,2,2,3,3,4]
new_nums = []
for num in nums:
    if num not in new_nums:
        new_nums.append(num)
print(new_nums)