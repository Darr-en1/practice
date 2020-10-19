class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:len(s)] + s[0:n]
