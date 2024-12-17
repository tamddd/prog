class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #0同じ数字を
        count = {}
        ret = 0

        for i in nums:
            if i in count:
                ret += count[i]
            count.setdefault(i, 0)
            count[i] += 1
        return ret
