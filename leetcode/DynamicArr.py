class DynamicArray:
    def __init__(self, capacity: int):
        self.arr = [False for _ in range(capacity)]
        self.cap = capacity
        self.now = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # size over
        if self.cap <= self.now:
            self.resize()
        self.arr[self.now] = n
        self.now += 1

    def popback(self) -> int:
        tmp = self.now - 1
        self.now -= 1
        return self.arr[tmp]

    def resize(self) -> None:
        # 2倍に
        self.arr = self.arr + [False for _ in range(self.cap)]
        self.cap *= 2

    def getSize(self) -> int:
        return self.now

    def getCapacity(self) -> int:
        return self.cap
