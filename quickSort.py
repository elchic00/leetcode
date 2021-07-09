#from random import choice 
#def sortArray( nums): #This version will use extra space to store the left and right side of the pivot.
        #if len(nums) <= 1:
            #return nums
        #pivot_ind = choice(range(len(nums)))
        #print(pivot_ind)
        #pivot = nums[pivot_ind]
 
        #left = [nums[i] for i in range(len(nums)) if nums[i] <= pivot and i != pivot_ind]
        #right = [nums[i] for i in range(len(nums)) if nums[i] > pivot]
        #return sortArray(left) + [pivot] + sortArray(right)

def quicksort(start , stop,arr): #This will sort the array in place with swapping, but is not using random for pivot causing less optimal average runtime. 
    if(start < stop):
        # pivotindex is the index where
        # the pivot lies in the array
        p = partition(start,stop,arr)
        
        quicksort(start,p-1,arr)
        quicksort(p+1,stop,arr)  
                
def partition(start,stop,arr):
    
    pivot_ind = start
    pivot = arr[pivot_ind]
            
    while start<stop:
                
        while start < len(arr) and arr[start] <= pivot:
            start += 1
            while arr[stop] > pivot:
                stop -=1
                if start<stop:
                    arr[start], arr[stop] = arr[stop] , arr[start]
                
    arr[stop], arr[pivot_ind] =arr[pivot_ind],  arr[stop]
    return stop

arr = [5,3,2,1]
quicksort(0,len(arr)-1,arr)
print(arr)
#print(sortArray([43,2,1,3,6]))
