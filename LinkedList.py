class Node:
    def __init__(self, val, nex=None):
        self.val = val
        self.nex = nex


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        cur = self.head
        if cur is None:
            return -1
        for _ in range(index):
            if cur is None:
                return -1
            cur = cur.nex
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            node.nex = self.head
            self.head = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.nex:
                cur = cur.nex
            cur.nex = node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.nex
            return True

        cur = self.head
        pre = None
        for _ in range(index):
            pre = cur
            cur = cur.nex
            if cur is None:
                return False
        pre.nex = cur.nex
        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.head
        while cur:
            res.append(cur.val)
            cur = cur.nex
        return res
