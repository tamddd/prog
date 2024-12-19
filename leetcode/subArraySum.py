class Solution:
    import bisect
    def subarraySum(self, nums: List[int], k: int) -> int:
        vis = {}
        vis[0] = 1
        cnt = 0
        now = 0
        for i in range(len(nums)):
            now += nums[i]
            if now - k in vis:
                cnt += vis[now-k]
            if now not in vis:vis[now] = 0
            vis[now] += 1
        return cnt
