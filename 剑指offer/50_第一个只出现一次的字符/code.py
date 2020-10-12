from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> str:
        exist = Counter(s)
        for nu in s:
            if exist[nu] == 1:
                return nu

        return " "

    def firstUniqChar1(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]:
                return c
        return " "
