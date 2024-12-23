class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tot = nums[0]
        left = 0
        right = 1
        res = M = 1001001001
        if tot >= target:
            res = 1
        while right < len(nums):
            while tot < target and right < len(nums):
                tot += nums[right]
                right += 1
            print(left, right)
            while tot >= target and left < right:
                res = min(res, right-left)
                tot -= nums[left]
                left += 1

        return res if res != M else 0
