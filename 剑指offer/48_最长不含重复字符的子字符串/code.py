class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        start = curr = 0
        _len = 0
        while curr <= len(s) - 1:

            while s[curr] in window:
                window.remove(s[start])
                start += 1
            window.add(s[curr])
            curr += 1
            _len = max(curr - start, _len)
        return _len


print(Solution().lengthOfLongestSubstring("pwwkew"))
