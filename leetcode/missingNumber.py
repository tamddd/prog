class Solution:
    #set
    def missingNumber(self, nums: List[int]) -> int:
        sn = set(nums)
        for i in range(len(nums) + 1):
            if i not in sn:
                return i
        return -1
