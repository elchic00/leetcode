#Bubble sort algo

n = int(input().strip()) #input the size of the array
a = list(map(int, input().strip().split(' ')))  #takes in a list of integers and maps it into an array. The input is split by a space, for ex: 1 2 3 4

print(n , a)

numSwaps = 0
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            numSwaps += 1
            a[j], a[j + 1] = a[j + 1], a[j]

print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n - 1]))
print(a)
