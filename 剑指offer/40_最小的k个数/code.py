from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 二分法
        def inner(start, end):
            begin = start
            for i in range(start + 1, end):
                if arr[start] > arr[i]:
                    arr[begin + 1], arr[i] = arr[i], arr[begin + 1]
                    begin += 1
            arr[begin], arr[start] = arr[start], arr[begin]
            if begin > k - 1:
                return inner(start, begin)
            elif begin < k - 1:
                return inner(begin + 1, end)
            else:
                return arr[0:begin + 1]

        return inner(0, len(arr))


print(Solution().getLeastNumbers([0, 0, 0, 2, 0, 5], 0))
