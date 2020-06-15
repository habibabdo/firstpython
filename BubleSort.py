

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp





nums=[5,3,8,6,7,2,1,22,34,34,25,675,88]
nums1=nums

print('Before Sort NUMS :  ',nums)
print('Before Sort NUMS1:  ',nums1)
sort(nums)
print()
nums1.sort()
print('After Sort NUMS1:   ',nums1)
print('After Sort NUMS :   ',nums)




