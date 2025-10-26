class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndWord = True

    def search(self, word):
        def dfs(start, root):
            cur = root

            for i in range(start, len(word)):
                c = word[i]
                if c == ".":
                    return any([dfs(i + 1, child) for child in cur.children.values()])
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEndWord

        return dfs(0, self.root)
