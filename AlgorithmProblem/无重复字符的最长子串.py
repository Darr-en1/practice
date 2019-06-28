class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set()
        left = 0
        max_len = 0
        cur_len = 0
        for idx, val in enumerate(s):
            while val in str_set:
                str_set.remove(s[left])
                left += 1
                cur_len -= 1
            cur_len += 1
            str_set.add(val)
            if cur_len > max_len: max_len = cur_len
        return max_len


if __name__ == '__main__':
    max_len = Solution().lengthOfLongestSubstring('sdsdsad')
    print(max_len)
