

# Naive function to find the maximum difference between two elements in
# a list such that the smaller element appears before the larger element
def maxDiff(arr):
    max_diff = arr[1] - arr[0]

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > max_diff:
                max_diff = arr[j] - arr[i]
    # if max_diff <= 0:
    #     return -1

    return max_diff


# Driver program to test above function
n = int(input("Enter number of days you will look at closing price for a stock: "))
arr = list(map(int,input("\nEnter the closing price for each day: ").strip().split()))[:n]
print(arr)
print("Maximum difference is", maxDiff(arr))
