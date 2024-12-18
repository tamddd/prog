class Solution:
    def maxScore(self, s: str) -> int:
        #右の０と左の１
        zero_counts = [0]
        one_counts = [0]
        

        for i in s:
            zero_counts.append(zero_counts[-1] + (1 if i == "0" else 0))
            one_counts.append(one_counts[-1] + (1 if i == "1" else 0))
        total_one = one_counts[-1]

        n = len(s)
        res = 0
        for i in range(1, n):
            res = max(res, zero_counts[i] + total_one - one_counts[i])
        return res
