# https://gyazo.com/5c6ad0514e7f25a4cd4d2ab4d6bbf688

#!/usr/bin/env python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

def input_binary_tree():
    input_values = input().split()
    index = 0
    num_nodes = int(input_values[index])
    index += 1
    if (num_nodes == 0):
        return None
        
    nodes = []
    current_parent_index = 0
    
    root = TreeNode(int(input_values[index]))
    index += 1
    nodes.append(root)
    
    for i in range(1, num_nodes, 2):
        left_val = int(input_values[index])
        index += 1
        if (left_val != -1):
            left = TreeNode(left_val)
            nodes.append(left)
            nodes[current_parent_index].left = left
        
        right_val = int(input_values[index])
        index += 1
        if (right_val != -1):
            right = TreeNode(right_val)
            nodes.append(right)
            nodes[current_parent_index].right = right
        
        current_parent_index += 1
        
    return root

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None
"""
from collections import deque
def average_of_levels(root):
    """
    Write your code here
    :type root: TreeNode
    :rtype: List[double]
    """
    que = deque([root])
    outp = []
    vals = 0
    while que:
        vals = 0
        for node in que:
            vals += node.val
        outp.append(vals/len(que))
        for _ in range(len(que)):
            cur = que.popleft()
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
    return outp
    
    
    
    

root = input_binary_tree()
