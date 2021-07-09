from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0: return 0
        
    i = 0
    j = i +1
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    print(i + 1)
    print(nums[:i+1])
    

arr = [1,1,1,1,2,2,3,4,4,4,5]
print(arr)
removeDuplicates(arr)
       
