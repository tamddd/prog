from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        deq = deque([(root, 1)])
        max_total = float('-inf')
        cur_level = 0
        res = 1
        total = max_total

        while deq:
            node, level = deq.popleft()

            if level != cur_level:
                if total > max_total:
                    max_total = total
                    res = cur_level
                cur_level = level
                total = node.val
            else:
                total += node.val

            if node.left:
                deq.append((node.left, level + 1))
            if node.right:
                deq.append((node.right, level + 1))

        if total > max_total:
            max_total = total
            res = cur_level

        return res
