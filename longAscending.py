def longestAscending(nums):
    if len(nums) == 1:
        return 1
    
    currLen = 1
    maxLen = 0
    
    for ind in range(len(nums)-1):
        if nums[ind + 1] > nums[ind]:
            currLen += 1
        else:
            maxLen = max(maxLen, currLen)
            currLen = 1
    
    return max(maxLen, currLen)
    



    
print(longestAscending([1,5,10,11]))
print(longestAscending([1,8,11,13,1,2,3]))
print(longestAscending([1,5,1,5,10]))
print(longestAscending([1,8,11,13, 1,2,3,4,5,6,7, 1,2,3,4,5,6,7,8,9, 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]))

'''
// int longestAscending(collectionOfNumbers)
//
// Input:
//   collectionOfNumbers -
//     An ordered set of integers which contains at least one integer.
//
// Output:
//   Returns the length of the longest subset of numbers in which the numbers
//   are in asending order.
//
// Examples:
//   collectionOfNumbers = {1,5,10} -> longestAscending(collectionOfNumbers) returns 3
//   collectionOfNumbers = {1,8,11,13,1,2,3} -> longestAscending(collectionOfNumbers) returns 4

'''
