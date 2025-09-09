from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        plus_pos = [0] * n
        for i in range(2**n):    
            for j in range(n):
                if (i >> j) & 1:
                    plus_pos[j] = 1
                else:
                    plus_pos[j] = 0
            tot = 0
            for j in range(n):
                if plus_pos[j] == 1:
                    tot += nums[j]
                else:
                    tot -= nums[j]
            if tot == target:
                res += 1
        return res
