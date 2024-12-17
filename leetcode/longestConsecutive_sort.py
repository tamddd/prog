class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sortする
        res = cnt = 0
        pre = (10**9) + 10
        for num in sorted(list(set(nums))):
            if pre + 1 == num:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
            pre = num
        return max(res, cnt)
