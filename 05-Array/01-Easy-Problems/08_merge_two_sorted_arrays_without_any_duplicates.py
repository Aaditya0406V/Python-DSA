nums1 = [1,1,1,2,3,6,8,9]
nums2 = [1,2,4,7,8]

def merge_two_sorted_array_without_any_duplicates(nums1,nums2):
    res = []
    i,j=0,0
    n,m=len(nums1),len(nums2)
    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(res) == 0 or res[-1]!=nums1[i]:
                res.append(nums1[i])
            i+=1
        else:
            if len(res) == 0 or res[-1]!=nums2[j]:
                res.append(nums2[j])
            j+=1
    if i<n:
        while i<n:
            if res[-1]!=nums1[i]:
                res.append(nums1[i])
            i+=1
    if j<m:
        while j<m:
            if res[-1]!=nums2[j]:
                res.append(nums2[j])
            j+=1
    return res

res = merge_two_sorted_array_without_any_duplicates(nums1,nums2)
print(res)