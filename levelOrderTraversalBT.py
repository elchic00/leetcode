from collections import deque
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Function to print leaf
# nodes from left to right
def levelOrder(root):
        if not root:
            return []
        queue = deque([root])
        outp = []
        while queue:
            outp.append([node.val for node in queue])
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return outp

# Driver Code
if __name__ == "__main__":

    # Let us create binary tree shown in
    # above diagram
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)

    print(levelOrder(root))
