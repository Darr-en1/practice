class Solution:
    """
    逻辑运算符的短路效应：
    常见的逻辑运算符有三种，即 “与 \&\&&& ”，“或 ||∣∣ ”，“非 !! ” ；而其有重要的短路效应，如下所示：


    if(A && B)  // 若 A 为 false ，则 B 的判断不会执行（即短路），直接判定 A && B 为 false

    if(A || B) // 若 A 为 true ，则 B 的判断不会执行（即短路），直接判定 A || B 为 true
    本题需要实现 “当 n = 1n=1 时终止递归” 的需求，可通过短路效应实现。


    n > 1 && sumNums(n - 1) // 当 n = 1 时 n > 1 不成立 ，此时 “短路” ，终止后续递归
    """

    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
