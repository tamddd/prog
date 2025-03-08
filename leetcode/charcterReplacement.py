class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        for c in set(s):
            cnt = 0
            left = 0
            for right in range(len(s)):
                if s[right] == c:
                    cnt += 1

                while (right - left + 1) - cnt > k:
                    if s[left] == c:
                        cnt -= 1
                    left += 1
                res = max(res, right - left + 1)
        return res
