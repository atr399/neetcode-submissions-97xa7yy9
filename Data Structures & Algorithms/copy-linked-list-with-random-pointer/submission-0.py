"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyToDict = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            copyToDict[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = copyToDict[cur]
            copy.next = copyToDict[cur.next]
            copy.random = copyToDict[cur.random]
            cur = cur.next

        return copyToDict[head]