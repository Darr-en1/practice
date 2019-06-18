class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        :type n: int
        :rtype: List[str]
        """
        res = set(['()'])
        for i in range(n - 1):
            tmp = set()
            for r in res:
                tmp.update(set([r[:j] + '()' + r[j:] for j in range(len(r))]))
            res = tmp
        return list(res)
