nums = [2,7,11,15]
target = 9
output=[]
stop=False
for i in range(len(nums)):
    if stop:
        break
    for j in range(i+1,len(nums)):
        if (nums[i]+nums[j])==target:
            output.append(i)
            output.append(j)
            stop=True
print(output)



