class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        sub = set()
        max_len = 0
        for r in range(len(s)):
            if s[r] not in sub:
                max_len = max(max_len, r - l + 1)
                sub.add(s[r])
            else:
                while s[r] in sub:
                    sub.remove(s[l])
                    l += 1
                sub.add(s[r])
        return max_len