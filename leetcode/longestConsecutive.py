class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ret = 0
        remove_nums = set()
        for num in nums_set:
            if num in remove_nums:continue
            cnt = 1

            #-方向
            minus_num = num-1
            while minus_num in nums_set and minus_num not in remove_nums:
                remove_nums.add(minus_num)
                minus_num -= 1
                cnt += 1
            #+方向
            plus_num = num+1
            while plus_num in nums_set and plus_num not in remove_nums:
                remove_nums.add(plus_num)
                plus_num += 1
                cnt += 1

            ret = max(ret, cnt)
        return ret
