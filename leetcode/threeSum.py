class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                sum_num = nums[i] + nums[left] + nums[right]
                if sum_num == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum_num < 0:
                    left += 1
                else:
                    right -= 1

        return list(ans)
