class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = right = 0
        n = len(nums)
        cnt = 0
        while right < n:
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                cnt += 1
            right += 1
        return cnt
