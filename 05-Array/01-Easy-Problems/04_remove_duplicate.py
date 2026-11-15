nums = [1,1,2,2,3,4,4,4,5,6,6,7,8]
i = 0
j = i+1

while j<len(nums):
            
    if nums[i]!=nums[j]:
        i+=1
        nums[i],nums[j]=nums[j],nums[i]
    j+=1
print(nums)
