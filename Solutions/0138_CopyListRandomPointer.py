# 138. Copy List with Random Pointer
# #LindedList
# Yuan-Peng Yu
# 01/25/2022

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # 1. Iterative
    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodeDict = {None : None} # store the current list (key, v) = (pointer, pointer)
        
        # 1. Instantiate each new node by traversing old list. Assign node values only. 
        curr = head 
        while curr:
            nodeDict[curr] = Node(curr.val)
            curr = curr.next
        
        # 2. connect the link of next & random
        curr = head
        while curr:
            nodeDict[curr].next = nodeDict[curr.next]
            nodeDict[curr].random = nodeDict[curr.random]
            curr = curr.next
            
        deepCopy = nodeDict[head]
        return deepCopy
    # Runtime: 36 ms, faster than 77.89% 
    # Memory Usage: 15 MB, less than 62.86%
    # Time: O(2n) = O(n)
    # Space: O(n)
 

    # 2. Recursive
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodeDict = dict()
        
        def deepCopy(node):
            
            if not node: return
            if node in nodeDict:    # existing node
                return nodeDict[node]
            
            # new node
            curr = Node(node.val)
            nodeDict[node] = curr
            curr.next = deepCopy(node.next)
            curr.random = deepCopy(node.random)
            return curr
        
        return  deepCopy(head)
    # Runtime: 36 ms, faster than 77.89% 
    # Memory Usage: 15.4 MB, less than 13.99%            
    # Time: O(n)
    # Space: O(n)
            
            

            