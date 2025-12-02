# アルゴ式 キューを配列で実装

n, q = map(int, input().split())

class Queue:
    def __init__(self, n):
        self.lst = [-1 for _ in range(n)]
        self.head = self.tail = 0
        self.length = n

    def push(self, val):
        self.lst[self.tail] = val
        self.tail += 1
        self.tail %= self.length

    def pop(self):
        self.lst[self.head] = -1
        self.head += 1
        self.head %= self.length

    def print_all(self):
        for i in self.lst:
            print(i)

    def pa(self):
        print(*self.lst)

queue = Queue(n)

for _ in range(q):
    que = list(map(int, input().split()))
    if que[0] == 0:
        queue.push(que[1])
    else:
        queue.pop()
    

queue.print_all()
