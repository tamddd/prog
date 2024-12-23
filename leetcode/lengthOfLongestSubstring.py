class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #重複のない
        slow = fast = 0
        res = cnt = 0
        vis = {}
        while fast < len(s):
            now_char = s[fast]
            if now_char not in vis:vis[now_char] = 0
            vis[now_char] += 1
            cnt += 1
            while vis[now_char] != 1:
                vis[s[slow]] -= 1
                slow += 1
                cnt -= 1
            res = max(res, cnt)
            fast += 1
        return res
