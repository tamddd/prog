class Solution:
    def getMinKth(self, bucket, x):
        for i in range(-50, 0):
            if i in bucket and bucket[i] != 0:
                x -= bucket[i]
            if x <= 0:
                return i
        return 0
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        bucket = {}
        for i in range(k):
            if nums[i] not in bucket:
                bucket[nums[i]] = 0
            bucket[nums[i]] += 1
        res.append(self.getMinKth(bucket, x))

        for i in range(k, n):
            #set num
            if nums[i] not in bucket:
                bucket[nums[i]] = 0
            bucket[nums[i]] += 1
            bucket[nums[i-k]] -= 1
            res.append(self.getMinKth(bucket, x))
        return res
