class UnionFind:
    def __init__(self, n=100):
        self.parent = [-1 for _ in range(n)]

    def union(self, x, y):
        x_parent = self.get_parent(x)
        y_parent = self.get_parent(y)

        if x_parent <= y_parent:
            self.parent[x] = y_parent
        else:
            self.parent[y] = x_parent

    def is_same(self, x, y):
        x_parent = self.get_parent(x)
        y_parent = self.get_parent(y)

        return x_parent == y_parent

    def get_parent(self, c):
        if self.parent[c] == -1:
            return c
        self.parent[c] = self.get_parent(self.parent[c])
        return self.parent[c]


if __name__ == "__main__":
    uf = UnionFind()
    uf.union(0, 1)
    uf.union(1, 2)
    print(uf.is_same(0, 4))
