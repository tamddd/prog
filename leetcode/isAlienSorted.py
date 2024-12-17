class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {c:i for i, c in enumerate(order)}
        return words == sorted(words, key=lambda s: [index[c] for c in s])
