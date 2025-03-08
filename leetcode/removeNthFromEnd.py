# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLength(self, node):
        node_length = 0
        while node:
            node = node.next
            node_length += 1
        return node_length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)
        length -= n

        if length == 0:
            head = head.next
            return head
        else:
            node = head
            while length != 1:
                length -= 1
                node = node.next
            node.next = node.next.next
            return head
