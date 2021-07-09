import collections
def intersect(nums1, nums2):
        if len(nums1) == 0 or len(nums2) == 0: #return to caller if either list has len == 0
            return
        
        hmap = collections.Counter(nums1) #Creates a dictionary to map each int in nums1 to the number of times it is counted in the list. Im using a dictionary counter to easily keep track of which numbers repeat in each list.
        outp = [] #Use this list to keep track of repeating characters
        for int in nums2: #Check if any of the ints in nums2 are already in the dict.
            if hmap[int] > 0: #If it does exist in our dict, then append it to our output list for our answer and decrement the counter value it maps to.
                hmap[int] -= 1 
                outp.append(int)
        return outp #Return a list of any ints that repeat in both strings.

n1 = [1,2,2,1]
n2 = [2,2]
print(intersect(n1,n2))
n1 = [4,9,5]
n2 = [9,4,9,8,4]
print(intersect(n1,n2))
n1 = []
n2 = [1]
print(intersect(n1,n2))
n1 = [2,3,4]
n2 = [1,5,6]
print(intersect(n1,n2)) 
#Time: O(n), Space:O(outp) 
