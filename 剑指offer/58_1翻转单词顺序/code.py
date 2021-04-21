class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        li = ""
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            li += s[i+1:j+1]
            if i >= 0:
                li += " "

            while s[i] == " ":
                i -= 1
            j = i

        return li


print(Solution().reverseWords("the sky is blue"))
