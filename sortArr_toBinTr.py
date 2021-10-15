class Node:

    def __init__(self, val =0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Function to print leaf
# nodes from left to right
def sortedArrayToBST(nums):
            if not nums:
                return 
            
            mid = len(nums)//2
            left =  sortedArrayToBST(nums[:mid])
            right = sortedArrayToBST(nums[mid+1:])
     
            return Node(nums[mid],left,right)
# Driver Code
if __name__ == "__main__":


    print(sortedArrayToBST([-1,-2,3,4,5,6]))
