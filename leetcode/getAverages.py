class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        n = len(nums)
        res = [-1 for _ in range(n)]
        if 2 * k + 1 > n:
            return res

        tot = 0
        for i in range(2 * k + 1):
            tot += nums[i]


        for i in range(k, n - k):
            res[i] = tot // (2 * k + 1)

            if i + k + 1 < n:
                tot -= nums[i-k]
                tot += nums[i+k+1]
        return res
