class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        tmp = self.head
        #whileでindex管理しながら回すよりも、forで
        for i in range(index):
            if tmp is None:
                return -1
            tmp = tmp.next
        return tmp.val if tmp else -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        tmp = self.head
        for i in range(index - 1):
            if tmp is None:
                return
            tmp = tmp.next
        if tmp:
            node = Node(val, tmp.next)
            tmp.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        tmp = self.head
        for i in range(index - 1):
            if tmp is None or tmp.next is None:
                return
            tmp = tmp.next
        if tmp.next:
            tmp.next = tmp.next.next
