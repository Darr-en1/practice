from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        a, res = list(s), []

        def inner(x):
            if x == len(a) - 1:
                res.append(''.join(a))
                return

            exist = set()
            for i in range(x, len(s)):
                if a[i] in exist:
                    continue

                exist.add(a[i])
                a[x], a[i] = a[i], a[x]
                inner(x + 1)
                a[x], a[i] = a[i], a[x]

        inner(0)
        return res


if __name__ == '__main__':
    a = "acbc"
    print(Solution().permutation(a))
