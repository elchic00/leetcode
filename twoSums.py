def twoSum(nums, target):
    dic = {}
    for ind, val in enumerate(nums):
        diff = target - val
        if diff in dic:
            return (dic[diff],ind)
        else:
            dic[val] = ind



arr = [1,2,3,4]
t = 7
print(arr,t)
print(twoSum(arr,t))
