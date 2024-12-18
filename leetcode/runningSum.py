class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0]
        for i in nums:
            res.append(res[-1] + i)

        return res[1:]
