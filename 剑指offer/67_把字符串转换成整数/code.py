class Solution:
    def strToInt(self, str: str) -> int:
        nmb = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        symbol = {"-", "+"}
        li = []
        for s in str:
            if not li:
                if s in symbol or s in nmb:
                    li.append(s)
                elif s == " ":
                    pass
                else:
                    return 0
            elif s in nmb:
                li.append(s)
            else:
                break
        res = "".join(li)
        res = 0 if not res or res in symbol else int(res)
        return 2 ** 31 - 1 if res > 2 ** 31 - 1 else -2 ** 31 if res < -2 ** 31 else res