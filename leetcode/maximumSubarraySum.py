class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        numPositions = {}
        n = len(nums)
        prefix = [0] * (n+1)
        res = -inf+1

        for i, v in enumerate(nums):
            print(i, v-k)
            prefix[i+1] = prefix[i] + nums[i]
            if (v-k) in numPositions:
                pi = numPositions[v-k]
                res = max(res, prefix[i+1] - prefix[pi])
            if (v+k) in numPositions:
                pi = numPositions[v+k]
                res = max(res, prefix[i+1] - prefix[pi])
            if v in numPositions and prefix[i+1] - prefix[numPositions[v]] < nums[i]:
                numPositions[v] = i
            if v not in numPositions:
                numPositions[v] = i
        return res if res != -inf+1 else 0
