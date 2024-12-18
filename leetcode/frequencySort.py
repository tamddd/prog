class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        res = []
        for i, v in sorted(counter.items(), key=lambda x : -x[1]):
            for j in range(v):
                res.append(i)
        return "".join(res)
