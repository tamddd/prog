class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapping_func(num):
            if num == 0:
                return mapping[num]
            ret = 0
            factor = 1
            while num != 0:
                ret = (factor * mapping[num%10]) + ret
                factor *= 10
                num //= 10
            return ret

        return sorted(nums, key=mapping_func)
