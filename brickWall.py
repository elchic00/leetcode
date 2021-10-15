# Understand
# Test1: [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Test2: [[1,2],[2,1],[3]] -> 2
# Test3: [[1,2],[1,1,1][2,1]] -> 1
# Test3: [[1,2][1,2][1,2]] -> 0
# Test4: [[3],[3],[3]] -> 3
# Test5: [] -> 0
# Test6: [[2,2]] -> 0
# Test7: [[2]] -> 1

# Match & Plan
#1: 1 3 5
#2:   34
#3: 1  4
#4:  2
#5:   34
#6: 1  45

# 1   2   3.  4.  5
# 3   1   3.  4.  2
# dicRow = {
#   1 : 3,
#   2: 1,
#   3: 3,
#   4: 4,
#   5: 2
# }
# Pseudocode
# dicRow = {}
# for each row:
#   cumsum = 0
#   for each elem:
#.    cumsum += elem
      # if dicRow[cumsum] does not exist:
      #   dicRow[cumsum] = 0
#     dicRow[cumsum] = dicRow[cumsum] + 1

# Read the Input

def BrickWall(wall) -> int:
  # n = int(input())
  # matrix = []
  # for i in range(n):
  #   matrix.append(list(map(int, input().split())))
  # print(matrix)
  n = len(wall)
  dicRow = {}
  for row in wall:
    cumsum = 0
    for i in range(len(row)-1):
      cumsum += row[i]
      if cumsum not in dicRow:
        dicRow[cumsum] = 0
      dicRow[cumsum] = dicRow[cumsum] + 1

  if dicRow:
    ans = n - max(dicRow.values())
  else:
    ans = n      
  return ans

print(BrickWall([[3],[3],[3]]))
print(BrickWall([[1,2],[2,1],[3]]))
print(BrickWall([[1,2],[1,1,1],[2,1]]))
print(BrickWall([[1,2],[1,2],[1,2]]))
print(BrickWall([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))








