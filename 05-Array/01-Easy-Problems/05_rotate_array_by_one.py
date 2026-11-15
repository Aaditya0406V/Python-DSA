nums = [1,1,2,2,3,4,4,4,5,6,6,7,8]
n = len(nums)
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp
print(nums)

# for python only using slicing

nums[:] = nums[n-1:]+nums[0:n-1]
print(nums)